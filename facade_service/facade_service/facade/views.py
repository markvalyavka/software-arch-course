from flask import request

from facade_service.facade import facade, helpers
from facade_service.gateways.logging_gateway import logging_gateway
from facade_service.gateways.messages_gateway import messages_gateway


@facade.route("/facade-service", methods=["GET", "POST"])
def facade_service():
    if request.method == "GET":
        logging_response = logging_gateway.get_messages()
        if not logging_response:
            return {
                "status": 'ERROR'
            }
        logging_msgs = logging_response.get("messages")
        messages_response = messages_gateway.get_messages()
        messages_msgs = messages_response.get("messages")
        return f"{logging_msgs}: {messages_msgs}"
    elif request.method == "POST":
        request_params = request.get_json()
        if not request_params:
            return "Error!"
        msg = request_params.get('message')
        msg_with_uuid = helpers.create_message(msg)
        logging_gateway.send_message(msg_with_uuid)
        return {
            "status": 'OK'
        }

