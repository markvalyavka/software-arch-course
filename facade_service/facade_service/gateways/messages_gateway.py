from facade_service.gateways.base_gateway import BaseGateway


DEFAULT_MESSAGES_ENDPOINT = "/messages-service"


class MessagesGateway(BaseGateway):

    def __init__(self, app=None):
        self.base_paths = None
        super(MessagesGateway, self).__init__(app)

    def init_gateway(self, app):
        self.base_paths = [
            app.config['MESSAGES_SERVICE_GATEWAY_1'],
            app.config['MESSAGES_SERVICE_GATEWAY_2'],
        ]

    def get_messages(self):
        response = self._get(
            url=self._build_random_url(endpoint=DEFAULT_MESSAGES_ENDPOINT)
        )
        return response


messages_gateway = MessagesGateway()
