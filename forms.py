from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField
from wtforms import EmailField
from wtforms import SelectField
from wtforms import validators

class UserForm(Form):
    id= IntegerField('Id')
    nombre = StringField('Nombre', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4,max=10,message='Ingrese nombre valido')])
    apaterno = StringField('Apaterno', [
        validators.DataRequired(message='El campo es requerido')])
    amaterno = StringField('Amaterno', [
        validators.DataRequired(message='El campo es requerido')])
    telefono = StringField('Telefono', [
        validators.DataRequired(message='El campo es requerido')])
    email = EmailField('Correo', [
        validators.Email(message='Ingrese un correo valido')
    ])


class MaestroForm(Form):
    matricula = IntegerField('Matricula', [
        validators.DataRequired(message='El campo es requerido')
    ])
    nombre = StringField('Nombre', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=20, message='Ingrese nombre valido')
    ])
    apellidos = StringField('Apellidos', [
        validators.DataRequired(message='El campo es requerido')
    ])
    especialidad = StringField('Especialidad', [
        validators.DataRequired(message='El campo es requerido')
    ])
    email = EmailField('Correo', [
        validators.Email(message='Ingrese un correo valido')
    ])


class CursoForm(Form):
    nombre = StringField('Nombre', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=20, message='Ingrese nombre valido')
    ])
    descripcion = StringField('Descripcion', [
        validators.DataRequired(message='El campo es requerido')
    ])
    maestro_id = IntegerField('Maestro ID', [
        validators.DataRequired(message='El campo es requerido')
    ])


class CursoAlumnosForm(Form):
    curso_id = SelectField('Curso', coerce=int, validators=[
        validators.DataRequired(message='Selecciona un curso válido')
    ])


class AlumnoCursosForm(Form):
    alumno_id = SelectField('Alumno', coerce=int, validators=[
        validators.DataRequired(message='Selecciona un alumno válido')
    ])


class InscripcionForm(Form):
    alumno_id = SelectField('Alumno', coerce=int, validators=[
        validators.DataRequired(message='Selecciona un alumno válido')
    ])
    curso_id = SelectField('Curso', coerce=int, validators=[
        validators.DataRequired(message='Selecciona un curso válido')
    ])



