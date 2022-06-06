import random
from urllib.parse import urljoin

from facade_service.gateways.base_gateway import BaseGateway


DEFAULT_LOGGING_ENDPOINT = "/logging-service"


class LoggingGateway(BaseGateway):

    def __init__(self, app=None):
        self.base_paths = None
        super(LoggingGateway, self).__init__(app)

    def init_gateway(self, app):
        self.base_paths = [
            app.config['LOGGING_SERVICE_GATEWAY_1'],
            app.config['LOGGING_SERVICE_GATEWAY_2'],
            app.config['LOGGING_SERVICE_GATEWAY_3'],
        ]

    def send_message(self, message):
        self._post(
            url=self._build_random_url(endpoint=DEFAULT_LOGGING_ENDPOINT),
            payload=message
        )

    def get_messages(self):
        response = self._get(
            url=self._build_random_url(endpoint=DEFAULT_LOGGING_ENDPOINT)
        )
        return response


logging_gateway = LoggingGateway()



