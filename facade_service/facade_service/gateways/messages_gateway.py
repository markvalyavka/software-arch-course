from facade_service.gateways.base_gateway import BaseGateway


DEFAULT_MESSAGES_ENDPOINT = "/messages-service"


class MessagesGateway(BaseGateway):

    def __init__(self, app=None):
        super(MessagesGateway, self).__init__(app)

    def init_gateway(self, app):
        self.base_path = app.config['MESSAGES_SERVICE_GATEWAY']

    def get_messages(self):
        response = self._get(
            url=self._build_url(endpoint=DEFAULT_MESSAGES_ENDPOINT)
        )
        return response


messages_gateway = MessagesGateway()
