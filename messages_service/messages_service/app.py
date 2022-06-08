import os

from flask import Flask

from messages_service.messages import messages
from messages_service.consul_api import c


def init_app():

    app = Flask(__name__)

    # load config
    app.config.from_object('messages_service.config.DebugConfig')

    # consul
    c.init_app(app)
    c.register_service(
        ip=c.get_host_ip(),
        port=5003,
        service_id=os.environ['SERVICE_ID']
    )

    # register blueprints
    app.register_blueprint(messages)

    @app.route("/")
    @app.route("/_health")
    def index():
        return {
            "status": "OK"
        }

    return app
