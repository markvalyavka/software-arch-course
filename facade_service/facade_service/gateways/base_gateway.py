import logging

import requests
from abc import ABC, abstractmethod
from urllib.parse import urljoin


class GatewayException(Exception):
    pass


class BaseGateway(ABC):

    # 15 sec timeout
    DEFAULT_REQUEST_TIMEOUT = 15

    def __init__(self, app=None):
        self.base_path = None
        if app is not None:
            self.init_gateway(app)

    @abstractmethod
    def init_gateway(self, app):
        raise NotImplementedError

    def _build_url(self, endpoint):
        url = urljoin(self.base_path, endpoint)
        return url

    @staticmethod
    def _get(url, timeout=DEFAULT_REQUEST_TIMEOUT):
        try:
            response = requests.get(
                url=url,
                timeout=timeout
            )
            response_json = response.json()
            response.raise_for_status()
            return response_json
        except requests.exceptions.HTTPError:
            raise GatewayException
        except Exception:
            logging.error("Error!")
            print("error!")

    @staticmethod
    def _post(url, payload, timeout=DEFAULT_REQUEST_TIMEOUT):
        try:
            response = requests.post(
                url=url,
                json=payload,
                timeout=timeout
            )
            response_json = response.json()
            response.raise_for_status()
            return response_json
        except requests.exceptions.HTTPError:
            raise GatewayException
        except Exception:
            logging.error("Error!")
            print("error!")
