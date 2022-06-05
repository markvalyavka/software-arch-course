from flask import Blueprint

messages = Blueprint(
    "messages",
    __name__,
    url_prefix=""
)

from . import views # noqa