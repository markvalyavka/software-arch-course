"""Configs for Flask app."""


class DebugConfig:

    # Logging services
    LOGGING_SERVICE_GATEWAY_1 = "http://logging-service-1:5002"
    LOGGING_SERVICE_GATEWAY_2 = "http://logging-service-2:5002"
    LOGGING_SERVICE_GATEWAY_3 = "http://logging-service-3:5002"

    # Messages services
    MESSAGES_SERVICE_GATEWAY_1 = "http://messages-service-1:5003"
    MESSAGES_SERVICE_GATEWAY_2 = "http://messages-service-2:5003"

    # RabbitMQ
    RABBITMQ_URL = 'host.docker.internal'
    # RABBITMQ_URL = '127.0.0.1'
