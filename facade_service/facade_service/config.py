"""Configs for Flask app."""


class DebugConfig:
    LOGGING_SERVICE_GATEWAY_1 = "http://logging-service-1:5002"
    LOGGING_SERVICE_GATEWAY_2 = "http://logging-service-2:5002"
    LOGGING_SERVICE_GATEWAY_3 = "http://logging-service-3:5002"
    MESSAGES_SERVICE_GATEWAY = "http://messages-service-1:5003"
