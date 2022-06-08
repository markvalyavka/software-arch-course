from facade_service.gateways.base_gateway import BaseGateway
from facade_service.consul_api import c


DEFAULT_MESSAGES_ENDPOINT = "/messages-service"


class MessagesGateway(BaseGateway):

    def get_random_messages_service_url(self, endpoint):
        healthy_services = c.discover_services("messages_service")
        print("---------------------------------")
        print(f"Healthy message services: {healthy_services}")
        url = self._build_random_url(
            hosts=healthy_services,
            endpoint=endpoint
        )
        print(f"Chosen: ", url)
        print("---------------------------------")
        return url

    def get_messages(self):
        url = self.get_random_messages_service_url(DEFAULT_MESSAGES_ENDPOINT)
        response = self._get(
            url=url
        )
        return response


messages_gateway = MessagesGateway()
