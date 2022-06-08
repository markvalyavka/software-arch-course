import json

from flask import request

from facade_service.facade import facade, helpers
from facade_service.gateways.logging_gateway import logging_gateway
from facade_service.gateways.messages_gateway import messages_gateway
from facade_service.rabbitmq import mq
from facade_service.consul_api import c


@facade.route("/facade-service", methods=["GET", "POST"])
def facade_service():
    if request.method == "GET":
        logging_response = logging_gateway.get_messages()
        messages_response = messages_gateway.get_messages()
        if logging_response is None or messages_response is None:
            return {
                "status": 'ERROR'
            }
        logging_msgs = logging_response.get("messages")
        messages_msgs = messages_response.get("messages")
        return f"{logging_msgs}: {messages_msgs}"
    elif request.method == "POST":
        request_params = request.get_json()
        if not request_params:
            return {
                "status": 'ERROR'
            }
        msg = request_params.get('message')
        msg_with_uuid = helpers.create_message(msg)
        logging_gateway.send_message(msg_with_uuid)
        mq.publish_msg(
            rk=c.get_kv('RABBITMQ_QUEUE_NAME'),
            msg_body=json.dumps(msg_with_uuid)
        )
        return {
            "status": 'OK'
        }

