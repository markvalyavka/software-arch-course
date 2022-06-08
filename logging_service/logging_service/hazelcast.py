import logging

import hazelcast

from logging_service.consul_api import c


class HazelcastClient:
    def __init__(self):
        self._cluster_url = None
        self._client = None

    def init_app(self, app):
        client = hazelcast.HazelcastClient(
            cluster_members=[
                c.get_kv('HAZELCAST_CLIENT_URL'),
            ],
            cluster_name=c.get_kv('HAZELCAST_CLIENT_CLUSTER_NAME'),
        )
        print("Successfully connected to hazelcast cluster.")
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

