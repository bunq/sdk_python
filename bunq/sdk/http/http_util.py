from typing import Dict


class HttpUtil:
    QUERY_FORMAT = '{}={}'
    QUERY_DELIMITER = '&'

    @classmethod
    def create_query_string(cls, all_parameter: Dict[str, str]):
        encoded_parameters = []

        for parameter in all_parameter:
            encoded_parameters.append(cls.QUERY_FORMAT.format(parameter, all_parameter[parameter]))

        return cls.QUERY_DELIMITER.join(encoded_parameters)
