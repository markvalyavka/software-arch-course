from messages_service.messages import messages


@messages.route("/messages-service")
def messages():
    return {
        "messages": "Not implemented yet!"
    }
