"""Configs for Flask app."""


class DebugConfig:
    HAZELCAST_CLIENT_URL = "host.docker.internal"
    HAZELCAST_CLIENT_CLUSTER_NAME = "dev"