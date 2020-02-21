from __future__ import annotations

import base64
import hmac
import re
import typing
from base64 import b64encode
from hashlib import sha1
from typing import Dict, List

from Cryptodome import Cipher
from Cryptodome import Random
from Cryptodome.Cipher import AES
from Cryptodome.Cipher import PKCS1_v1_5 as PKCS1_v1_5_Cipher
from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA
from Cryptodome.PublicKey.RSA import RsaKey
from Cryptodome.Signature import PKCS1_v1_5

from bunq.sdk.exception.bunq_exception import BunqException

if typing.TYPE_CHECKING:
    from bunq.sdk.context.api_context import ApiContext

# Error constants.
_ERROR_INVALID_SIGNATURE = 'Could not validate response signature.'

# Size of private RSA key to generate
_RSA_KEY_SIZE = 2048

# Constants to perform re-encoding of the public key
_PATTERN_RSA = r' RSA '
_REPLACEMENT_RSA = ' '

# Number of PKCS to use for exporting the private key
_PKCS_NUMBER_PRIVATE_KEY = 8

# Constants to generate request head string
_FORMAT_METHOD_AND_ENDPOINT = '{} /v1/{}\n'
_FORMAT_HEADER_STRING = '{}: {}\n'
_DELIMITER_NEWLINE = '\n'

# Constants for building header string to sign
_PATTERN_HEADER_PREFIX_BUNQ = r'X-Bunq-'
_HEADER_CACHE_CONTROL = 'Cache-Control'
_HEADER_USER_AGENT = 'User-Agent'

# Constants for AES encryption
_AES_KEY_SIZE = 32
_BLOCK_SIZE = 16

# Regex constants
_REGEX_FOR_LOWERCASE_HEADERS = r'(-[a-z])'

# Encryption-specific headers
_HEADER_CLIENT_ENCRYPTION_KEY = 'X-Bunq-Client-Encryption-Key'
_HEADER_CLIENT_ENCRYPTION_IV = 'X-Bunq-Client-Encryption-Iv'
_HEADER_CLIENT_ENCRYPTION_HMAC = 'X-Bunq-Client-Encryption-Hmac'
_HEADER_SERVER_SIGNATURE = 'X-Bunq-Server-Signature'

def generate_rsa_private_key() -> RsaKey:
    return RSA.generate(_RSA_KEY_SIZE)


def public_key_to_string(public_key: RsaKey) -> str:
    return re.sub(
        _PATTERN_RSA,
        _REPLACEMENT_RSA,
        public_key.exportKey().decode()
    )


def private_key_to_string(private_key: RsaKey) -> str:
    return private_key.exportKey(pkcs=_PKCS_NUMBER_PRIVATE_KEY).decode()


def rsa_key_from_string(string: str) -> RsaKey:
    return RSA.import_key(string)


def sign_request(private_key: RsaKey,
                 body_bytes: bytes) -> str:
    signer = PKCS1_v1_5.new(private_key)
    digest = SHA256.new()
    digest.update(body_bytes)
    sign = signer.sign(digest)

    return b64encode(sign)


def _generate_request_head_bytes(method: str,
                                 endpoint: str,
                                 headers: Dict[str, str]) -> bytes:
    head_string = _FORMAT_METHOD_AND_ENDPOINT.format(method, endpoint)
    header_tuples = sorted((k, headers[k]) for k in headers)

    for name, value in header_tuples:
        if _should_sign_request_header(name):
            head_string += _FORMAT_HEADER_STRING.format(name, value)

    return (head_string + _DELIMITER_NEWLINE).encode()


def _should_sign_request_header(header_name: str) -> bool:
    if header_name in {_HEADER_USER_AGENT, _HEADER_CACHE_CONTROL}:
        return True

    if re.match(_PATTERN_HEADER_PREFIX_BUNQ, header_name):
        return True

    return False


def generate_signature(string_to_sign: str, key_pair: RsaKey) -> str:
    bytes_to_sign = string_to_sign.encode()
    signer = PKCS1_v1_5.new(key_pair)
    digest = SHA256.new()
    digest.update(bytes_to_sign)
    sign = signer.sign(digest)

    return b64encode(sign)


def encrypt(api_context: ApiContext,
            request_bytes: bytes,
            custom_headers: Dict[str, str]) -> bytes:
    key = Random.get_random_bytes(_AES_KEY_SIZE)
    iv = Random.get_random_bytes(_BLOCK_SIZE)
    _add_header_client_encryption_key(api_context, key, custom_headers)
    _add_header_client_encryption_iv(iv, custom_headers)
    request_bytes = _encrypt_request_bytes(request_bytes, key, iv)
    _add_header_client_encryption_hmac(request_bytes, key, iv, custom_headers)

    return request_bytes


def _add_header_client_encryption_key(api_context: ApiContext,
                                      key: bytes,
                                      custom_headers: Dict[str, str]) -> None:
    public_key_server = api_context.installation_context.public_key_server
    key_cipher = PKCS1_v1_5_Cipher.new(public_key_server)
    key_encrypted = key_cipher.encrypt(key)
    key_encrypted_base64 = base64.b64encode(key_encrypted).decode()
    custom_headers[_HEADER_CLIENT_ENCRYPTION_KEY] = key_encrypted_base64


def _add_header_client_encryption_iv(iv: bytes,
                                     custom_headers: Dict[str, str]) -> None:
    custom_headers[_HEADER_CLIENT_ENCRYPTION_IV] = base64.b64encode(iv).decode()


def _encrypt_request_bytes(request_bytes: bytes,
                           key: bytes,
                           iv: bytes) -> bytes:
    cipher = Cipher.AES.new(key, Cipher.AES.MODE_CBC, iv)
    request_bytes_padded = _pad_bytes(request_bytes)

    return cipher.encrypt(request_bytes_padded)


def _pad_bytes(request_bytes: bytes) -> bytes:
    padding_length = (_BLOCK_SIZE - len(request_bytes) % _BLOCK_SIZE)
    padding_character = bytes(bytearray([padding_length]))

    return request_bytes + padding_character * padding_length


def _add_header_client_encryption_hmac(request_bytes: bytes,
                                       key: bytes,
                                       iv: bytes,
                                       custom_headers: Dict[str, str]) -> None:
    hashed = hmac.new(key, iv + request_bytes, sha1)
    hashed_base64 = base64.b64encode(hashed.digest()).decode()
    custom_headers[_HEADER_CLIENT_ENCRYPTION_HMAC] = hashed_base64


def validate_response(public_key_server: RsaKey,
                      status_code: int,
                      body_bytes: bytes,
                      headers: Dict[str, str]) -> None:
    if is_valid_response_header_with_body(public_key_server, status_code, body_bytes, headers):
        return
    elif is_valid_response_body(public_key_server, body_bytes, headers):
        return
    else:
        raise BunqException(_ERROR_INVALID_SIGNATURE)


def is_valid_response_header_with_body(public_key_server: RsaKey,
                                       status_code: int,
                                       body_bytes: bytes,
                                       headers: Dict[str, str]) -> bool:
    head_bytes = _generate_response_head_bytes(status_code, headers)
    bytes_signed = head_bytes + body_bytes
    signer = PKCS1_v1_5.pkcs1_15.new(public_key_server)
    digest = SHA256.new()
    digest.update(bytes_signed)

    try:
        signer.verify(digest, base64.b64decode(headers[_HEADER_SERVER_SIGNATURE]))

        return True
    except ValueError:
        return False


def is_valid_response_body(public_key_server: RsaKey,
                      body_bytes: bytes,
                      headers: Dict[str, str]) -> bool:
    signer = PKCS1_v1_5.pkcs1_15.new(public_key_server)
    digest = SHA256.new()
    digest.update(body_bytes)

    try:
        signer.verify(digest, base64.b64decode(headers[_HEADER_SERVER_SIGNATURE]))

        return True
    except ValueError:
        return False


def _generate_response_head_bytes(status_code: int,
                                  headers: Dict[str, str]) -> bytes:
    head_string = str(status_code) + _DELIMITER_NEWLINE
    header_tuples = sorted((k, headers[k]) for k in headers)

    for name, value in header_tuples:
        name = _get_header_correctly_cased(name)

        if _should_sign_response_header(name):
            head_string += _FORMAT_HEADER_STRING.format(name, value)

    return (head_string + _DELIMITER_NEWLINE).encode()


def _get_header_correctly_cased(header_name: str) -> str:
    header_name = header_name.capitalize()

    matches = re.findall(_REGEX_FOR_LOWERCASE_HEADERS, header_name)

    for match in matches:
        header_name = (re.sub(match, match.upper(), header_name))

    return header_name


def _should_sign_response_header(header_name: str) -> bool:
    if header_name == _HEADER_SERVER_SIGNATURE:
        return False

    if re.match(_PATTERN_HEADER_PREFIX_BUNQ, header_name):
        return True

    return False


def get_certificate_chain_string(all_chain_certificate: List[str]):
    return _DELIMITER_NEWLINE.join(all_chain_certificate)
