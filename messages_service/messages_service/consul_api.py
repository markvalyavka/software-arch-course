import consul


class ConsulClient:

    def __init__(self):
        self._c = None

    def init_app(self, app):
        self._c = consul.Consul(
            host=app.config['CONSUL_SERVER_URL'],
            port=8500
        )

    def register_service(self, ip, port, service_id):

        self._c.agent.service.register(
            name="messages_service",
            address=ip,
            port=port,
            service_id=service_id,
            check=consul.Check.http(f'http://{ip}:{port}/_health', interval='5s'),
        )
        print("REGISTERRED FROM LOGGING")

    def get_kv(self, k):
        val = self._c.kv.get(k)
        if val is None:
            return None
        return val[1]['Value'].decode('utf-8')

    @staticmethod
    def get_host_ip():
        import socket
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip


c = ConsulClient()






