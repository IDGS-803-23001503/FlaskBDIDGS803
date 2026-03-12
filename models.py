## este sera mi ORM

import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Alumnos(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apaterno = db.Column(db.String(100), nullable=False)
    amaterno = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)
    cursos = db.relationship('Cursos', secondary='inscripciones', back_populates='alumnos', lazy='dynamic')

class Maestros(db.Model):
    __tablename__ = 'maestros'
    matricula = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    especialidad = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    cursos = db.relationship('Cursos', back_populates='maestro', cascade='all, delete-orphan', lazy='dynamic')


class Cursos(db.Model):
    __tablename__ = 'cursos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    maestro_id = db.Column(db.Integer, db.ForeignKey('maestros.matricula'), nullable=False)
    maestro = db.relationship('Maestros', back_populates='cursos')
    alumnos = db.relationship('Alumnos', secondary='inscripciones', back_populates='cursos', lazy='dynamic')

class Inscripciones(db.Model):
    __tablename__ = 'inscripciones'
    id = db.Column(db.Integer, primary_key=True)
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumnos.id'), nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'), nullable=False)
    fecha_inscripcion = db.Column(db.DateTime, default=datetime.datetime.now)
    alumno = db.relationship('Alumnos', backref=db.backref('inscripciones', lazy=True))
    curso = db.relationship('Cursos', backref=db.backref('inscripciones', lazy=True))
    __table_args__ = (db.UniqueConstraint('alumno_id', 'curso_id', name='uq_alumno_curso'),)