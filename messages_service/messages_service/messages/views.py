from messages_service.messages import messages
from messages_service.sqllite import sqlite_db


@messages.route("/messages-service")
def messages():
    return {
        "messages": sqlite_db.read_all_messages()
    }
