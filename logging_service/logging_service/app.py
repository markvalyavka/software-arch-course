import os

from flask import Flask

from logging_service.logging import logging
from logging_service.hazelcast import hz
from logging_service.consul_api import c


def init_app():

    app = Flask(__name__)

    # load config
    app.config.from_object('logging_service.config.DebugConfig')

    # consul
    c.init_app(app)
    c.register_service(
        ip=c.get_host_ip(),
        port=5002,
        service_id=os.environ['SERVICE_ID']
    )

    # init apps
    hz.init_app(app)

    # register blueprints
    app.register_blueprint(logging)

    @app.route("/")
    @app.route("/_health")
    def index():
        return {
            "status": "OK"
        }

    return app
