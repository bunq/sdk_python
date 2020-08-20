"""
A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# To use a consistent encoding
from codecs import open
from os import path

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bunq_sdk',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.14.1',

    description='bunq Python SDK',
    long_description=long_description,
    long_description_content_type="text/markdown",

    # The project's main homepage.
    url='https://github.com/bunq/sdk_python',

    # Author details
    author='bunq',
    author_email='support@bunq.com',

    # The project's license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',
    ],

    # Require Python version equal or higher than the requested version.
    python_requires='>=3.5.3',

    # Keywords related to the project
    keywords='open-banking sepa bunq finance api payment',

    # Packages of the project. "find_packages()" lists all the project packages.
    packages=find_packages(exclude=[
        'contrib',
        'docs',
        'tests',
        'examples',
        'assets',
        '.idea',
        'run.py'
    ]),

    # Run-time dependencies of the project. These will be installed by pip.
    install_requires=[
        'aenum>=2.2.4,<3.0.0',
        'chardet>=3.0.4,<4.0.0',
        'pycryptodomex>=3.9.8,<4.0.0',
        'requests>=2.24.0,<3.0.0',
        'simplejson>=3.17.2,<4.0.0',
        'urllib3>=1.25.10,<2.0.0'
    ],
)