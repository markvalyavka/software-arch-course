"""Helpers fro facade blueprint."""


import uuid


def create_message(msg):
    return {
        "uuid": str(uuid.uuid1()),
        "message": msg
    }

