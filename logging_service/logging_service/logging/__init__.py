from flask import Blueprint

logging = Blueprint(
    "logging",
    __name__,
    url_prefix=""
)

from . import views # noqa