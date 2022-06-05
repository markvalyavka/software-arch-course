from flask import Flask

from logging_service.logging import logging
from logging_service.hazelcast import hz


def init_app():

    app = Flask(__name__)

    # load config
    app.config.from_object('logging_service.config.DebugConfig')

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
