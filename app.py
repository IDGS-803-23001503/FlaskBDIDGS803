from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from config import DevelopmentConfig
from models import db, Alumnos, Maestros, Cursos, Inscripciones
from maestros.routes import maestros_bp
from cursos.routes import cursos_bp
from alumnos.routes import alumnos_bp
from reportes.routes import reportes_bp

app = Flask(__name__)			

app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect(app)
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(maestros_bp)
app.register_blueprint(cursos_bp)
app.register_blueprint(alumnos_bp)
app.register_blueprint(reportes_bp)

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html")



@app.route('/')
def home():
	return render_template('home.html')
			


if __name__ == '__main__':
	app.run(debug=True)


