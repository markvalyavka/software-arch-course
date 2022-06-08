import random
import requests
from urllib.parse import urljoin

from facade_service.consul_api import c


class GatewayException(Exception):
    pass


class BaseGateway:

    # 15 sec timeout
    DEFAULT_REQUEST_TIMEOUT = 15

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

    @staticmethod
    def _build_random_url(hosts, endpoint):
        url = urljoin(random.choice(hosts), endpoint)
        return url
