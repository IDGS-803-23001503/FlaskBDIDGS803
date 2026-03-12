from flask import render_template, request, redirect, url_for
import forms
from . import cursos as cursos_bp
from models import db, Cursos, Maestros


@cursos_bp.route('/cursos')
def index():
    cursos = Cursos.query.all()
    return render_template("cursos/index.html", cursos=cursos)


@cursos_bp.route('/cursos/crear', methods=['GET', 'POST'])
def crear():
    create_form = forms.CursoForm(request.form)
    maestros = Maestros.query.order_by(Maestros.nombre).all()
    if request.method == 'POST' and create_form.validate():
        maestro = Maestros.query.get(create_form.maestro_id.data)
        if maestro is None:
            create_form.maestro_id.errors.append('Selecciona un maestro válido.')
        else:
            curso = Cursos()
            curso.nombre = create_form.nombre.data
            curso.descripcion = create_form.descripcion.data
            curso.maestro_id = maestro.matricula
            db.session.add(curso)
            db.session.commit()
            return redirect(url_for('cursos.index'))
    return render_template("cursos/cursos.html", form=create_form, maestros=maestros)


@cursos_bp.route('/cursos/detalles/<int:id>')
def detalles(id):
    curso = Cursos.query.get_or_404(id)
    return render_template(
        "cursos/detalles.html",
        id=curso.id,
        nombre=curso.nombre,
        descripcion=curso.descripcion,
        maestro_id=curso.maestro_id
    )


@cursos_bp.route('/cursos/modificar/<int:id>', methods=['GET', 'POST'])
def modificar(id):
    curso = Cursos.query.get_or_404(id)
    create_form = forms.CursoForm(request.form, obj=curso)
    maestros = Maestros.query.order_by(Maestros.nombre).all()
    if request.method == 'POST' and create_form.validate():
        maestro = Maestros.query.get(create_form.maestro_id.data)
        if maestro is None:
            create_form.maestro_id.errors.append('Selecciona un maestro válido.')
        else:
            curso.nombre = create_form.nombre.data
            curso.descripcion = create_form.descripcion.data
            curso.maestro_id = maestro.matricula
            db.session.commit()
            return redirect(url_for('cursos.index'))
    return render_template("cursos/modificar.html", form=create_form, id=id, maestros=maestros)


@cursos_bp.route('/cursos/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar(id):
    curso = Cursos.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(curso)
        db.session.commit()
        return redirect(url_for('cursos.index'))
    return render_template("cursos/eliminar.html", curso=curso)