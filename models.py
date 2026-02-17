
## este sera mi ORM

import datetime
from tkinter import INSERT
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Alumno(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apaterno = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)


