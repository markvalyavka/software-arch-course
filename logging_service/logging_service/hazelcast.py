import logging

import hazelcast


class HazelcastClient:
    def __init__(self):
        self._cluster_url = None
        self._client = None

    def init_app(self, app):
        client = hazelcast.HazelcastClient(
            cluster_members=[
                app.config['HAZELCAST_CLIENT_URL'],
            ],
            cluster_name=app.config['HAZELCAST_CLIENT_CLUSTER_NAME']
        )
        logging.info("Successfully connected to hazelcast cluster.")
        self._client = client

    def get_blocking_map(self, name):
        return self._client.get_map(name).blocking()

    @property
    def client(self):
        if self._client is None:
            return "Client is not initialized."
        return self._client


hz = HazelcastClient()

