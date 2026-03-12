from flask import render_template, request, redirect, url_for, flash
from typing import Sequence
import forms
from . import reportes as reportes_bp
from models import Cursos, Alumnos, db


def _curso_choices() -> Sequence[tuple[str, str]]:
    return [
        (str(curso.id), f"{curso.nombre} ({curso.maestro.nombre})")
        for curso in Cursos.query.order_by(Cursos.nombre).all()
    ]


def _alumno_choices() -> Sequence[tuple[str, str]]:
    return [
        (str(alumno.id), f"{alumno.nombre} {alumno.apaterno}")
        for alumno in Alumnos.query.order_by(Alumnos.nombre).all()
    ]


@reportes_bp.route('/reportes', methods=['GET', 'POST'])
def panel():
    curso_form = forms.CursoAlumnosForm(request.form, prefix='curso')
    alumno_form = forms.AlumnoCursosForm(request.form, prefix='alumno')
    inscribir_form = forms.InscripcionForm(request.form, prefix='inscribir')
    curso_form.curso_id.choices = _curso_choices()
    alumno_form.alumno_id.choices = _alumno_choices()
    inscribir_form.curso_id.choices = curso_form.curso_id.choices
    inscribir_form.alumno_id.choices = alumno_form.alumno_id.choices

    curso_alumnos = None
    alumno_cursos = None
    selected_curso = None
    selected_alumno = None

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'curso' and curso_form.validate():
            selected_curso = Cursos.query.get(curso_form.curso_id.data)
            if selected_curso:
                curso_alumnos = selected_curso.alumnos.order_by(Alumnos.nombre).all()
        elif action == 'alumno' and alumno_form.validate():
            selected_alumno = Alumnos.query.get(alumno_form.alumno_id.data)
            if selected_alumno:
                alumno_cursos = selected_alumno.cursos.order_by(Cursos.nombre).all()
        elif action == 'inscribir' and inscribir_form.validate():
            alumno = Alumnos.query.get(inscribir_form.alumno_id.data)
            curso = Cursos.query.get(inscribir_form.curso_id.data)
            if alumno and curso:
                already = alumno.cursos.filter_by(id=curso.id).first()
                if already:
                    flash('El alumno ya está inscrito en el curso seleccionado.', 'warning')
                else:
                    alumno.cursos.append(curso)
                    db.session.commit()
                    flash('Alumno inscrito correctamente.', 'success')
            return redirect(url_for('reportes.panel'))

    return render_template(
        'reportes/index.html',
        curso_form=curso_form,
        alumno_form=alumno_form,
        inscribir_form=inscribir_form,
        curso_alumnos=curso_alumnos,
        alumno_cursos=alumno_cursos,
        selected_curso=selected_curso,
        selected_alumno=selected_alumno
    )
