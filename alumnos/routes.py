from flask import render_template, request, redirect, url_for
import forms
from . import alumnos as alumnos_bp
from models import db, Alumnos


@alumnos_bp.route('/alumnos')
def index():
    alumnos = Alumnos.query.order_by(Alumnos.created_date.desc()).all()
    return render_template('alumnos/index.html', alumno=alumnos)


@alumnos_bp.route('/alumnos/crear', methods=['GET', 'POST'])
def crear():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST' and create_form.validate():
        alumno = Alumnos()
        alumno.nombre = create_form.nombre.data
        alumno.apaterno = create_form.apaterno.data
        alumno.amaterno = create_form.amaterno.data
        alumno.telefono = create_form.telefono.data
        alumno.email = create_form.email.data
        db.session.add(alumno)
        db.session.commit()
        return redirect(url_for('alumnos.index'))
    return render_template('alumnos/crear.html', form=create_form)


@alumnos_bp.route('/alumnos/detalles/<int:id>')
def detalles(id):
    alumno = Alumnos.query.get_or_404(id)
    return render_template(
        'alumnos/detalles.html',
        nombre=alumno.nombre,
        apaterno=alumno.apaterno,
        amaterno=alumno.amaterno,
        correo=alumno.email
    )


@alumnos_bp.route('/alumnos/modificar/<int:id>', methods=['GET', 'POST'])
def modificar(id):
    alumno = Alumnos.query.get_or_404(id)
    create_form = forms.UserForm(request.form, obj=alumno)
    if request.method == 'POST' and create_form.validate():
        alumno.nombre = create_form.nombre.data
        alumno.apaterno = create_form.apaterno.data
        alumno.amaterno = create_form.amaterno.data
        alumno.telefono = create_form.telefono.data
        alumno.email = create_form.email.data
        db.session.commit()
        return redirect(url_for('alumnos.index'))
    create_form.id.data = alumno.id
    return render_template('alumnos/modificar.html', form=create_form)


@alumnos_bp.route('/alumnos/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar(id):
    alumno = Alumnos.query.get_or_404(id)
    create_form = forms.UserForm(obj=alumno)
    if request.method == 'POST':
        db.session.delete(alumno)
        db.session.commit()
        return redirect(url_for('alumnos.index'))
    create_form.id.data = alumno.id
    return render_template('alumnos/eliminar.html', form=create_form)
