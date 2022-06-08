from facade_service.gateways.base_gateway import BaseGateway
from facade_service.consul_api import c

DEFAULT_LOGGING_ENDPOINT = "/logging-service"


class LoggingGateway(BaseGateway):

    def get_random_logging_service_url(self, endpoint):

        healthy_services = c.discover_services("logging_service")
        #healthy_services = ["http://messages_service-1"]
        print("---------------------------------")
        print(f"Healthy logging services: {healthy_services}")
        url = self._build_random_url(
            hosts=healthy_services,
            endpoint=endpoint
        )
        print(f"Chosen: ", url)
        print("---------------------------------")
        return url

    def send_message(self, message):
        url = self.get_random_logging_service_url(DEFAULT_LOGGING_ENDPOINT)
        self._post(
            url=url,
            payload=message
        )

    def get_messages(self):
        url = self.get_random_logging_service_url(DEFAULT_LOGGING_ENDPOINT)
        response = self._get(
            url=url
        )
        return response


logging_gateway = LoggingGateway()



