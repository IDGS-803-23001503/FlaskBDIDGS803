from flask import Blueprint

maestros=Blueprint('maestros',
                    __name__,
                    template_folder='../templates/maestros',
                    static_folder='static')
from . import routes