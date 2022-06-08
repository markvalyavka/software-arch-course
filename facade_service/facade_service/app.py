import os

from flask import Flask, jsonify

from facade_service.facade import facade
from facade_service.rabbitmq import mq
from facade_service.consul_api import c


def init_app():
    app = Flask(__name__)

    # load config
    app.config.from_object('facade_service.config.DebugConfig')

    # consul
    c.init_app(app)
    c.register_service(
        ip=c.get_host_ip(),
        port=5001,
        service_id=os.environ['SERVICE_ID']
    )

    # init apps
    mq.init_app(app)

    # register blueprints
    app.register_blueprint(facade)

    @app.route("/")
    @app.route("/_health")
    def index():
        return jsonify({
            "status": "OK"
        })

    return app
