from flask import Blueprint

cursos=Blueprint('cursos',
                    __name__,
                    template_folder='../templates/cursos',
                    static_folder='static')
from . import routes