from typing import Dict


class HttpUtil:
    QUERY_FORMAT = '{}={}'
    QUERY_DELIMITER = '&'

    @classmethod
    def create_query_string(cls, all_parameter: Dict[str, str]):
        encoded_parameters = []

        for parameter, value in all_parameter.items():
            encoded_parameters.append(cls.QUERY_FORMAT.format(parameter, value))

        return cls.QUERY_DELIMITER.join(encoded_parameters)
