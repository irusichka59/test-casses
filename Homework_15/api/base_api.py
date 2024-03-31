import requests
import logging

logger = logging.getLogger(__name__)


class BaseApi:

    def __execute_request(self, method, url, params=None, body=None, headers=None, expected_status_code=None,
                          schema=None):
        logger.info(f'send {method} request to {url} with params {params}\nbody = {body}')
        response = requests.request(
            method=method,
            url=url,
            params=params or {},
            data=body,
            headers=headers or {}
        )
        logger.info(f'response is {response.status_code}')
        return response  # Оновлений рядок: повертаємо об'єкт requests.Response

    def get(self, url, params=None, headers=None, expected_status_code=None, schema=None):
        return self.__execute_request('get', url=url, params=params, headers=headers,
                                      expected_status_code=expected_status_code, schema=schema)

    def post(self, url, body=None, headers=None, expected_status_code=None, schema=None):
        return self.__execute_request('post', url=url, body=body, headers=headers,
                                      expected_status_code=expected_status_code, schema=schema)

    def put(self, url, body=None, headers=None, expected_status_code=None):
        return self.__execute_request('put', url=url, body=body, headers=headers,
                                      expected_status_code=expected_status_code)

    def patch(self, url, body=None, headers=None, expected_status_code=None):
        return self.__execute_request('patch', url=url, body=body, headers=headers,
                                      expected_status_code=expected_status_code)

    def delete(self, url, headers=None, expected_status_code=None):
        return self.__execute_request('delete', url=url, headers=headers,
                                      expected_status_code=expected_status_code)
