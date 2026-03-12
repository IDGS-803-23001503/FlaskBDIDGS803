from flask import Blueprint

reportes = Blueprint(
    'reportes',
    __name__,
    template_folder='../templates/reportes',
    static_folder='static'
)

from . import routes
