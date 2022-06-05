from flask import Flask, jsonify

from facade_service.facade import facade
from facade_service.gateways.logging_gateway import logging_gateway
from facade_service.gateways.messages_gateway import messages_gateway


def init_app():
    app = Flask(__name__)

    # load config
    app.config.from_object('facade_service.config.DebugConfig')

    # init app
    logging_gateway.init_gateway(app)
    messages_gateway.init_gateway(app)

    # register blueprints
    app.register_blueprint(facade)

    @app.route("/")
    @app.route("/_health")
    def index():
        return jsonify({
            "status": "OK"
        })

    return app
