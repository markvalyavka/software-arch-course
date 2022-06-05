from flask import Flask

from messages_service.messages import messages


def init_app():

    app = Flask(__name__)

    # register blueprints
    app.register_blueprint(messages)

    @app.route("/")
    @app.route("/_health")
    def index():
        return {
            "status": "OK"
        }

    return app
