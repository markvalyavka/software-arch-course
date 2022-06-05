from flask import Blueprint

facade = Blueprint(
    'facade',
    __name__,
    url_prefix=""
)

from . import views # noqa
