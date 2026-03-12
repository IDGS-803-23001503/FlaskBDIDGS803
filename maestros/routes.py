from flask import render_template, request, redirect, url_for
import forms
from . import maestros as maestros_bp
from models import db, Maestros



@maestros_bp.route('/maestros')
def index():
    maestros = Maestros.query.all()
    return render_template("maestros/index.html", maestros=maestros)


@maestros_bp.route('/maestros', methods=['GET', 'POST'])
def listar_maestros():
    create_form = forms.MaestroForm(request.form)
    if request.method == 'POST':
        maestro = Maestros()
        maestro.matricula = create_form.matricula.data
        maestro.nombre = create_form.nombre.data
        maestro.apellidos = create_form.apellidos.data
        maestro.especialidad = create_form.especialidad.data
        maestro.email = create_form.email.data
        db.session.add(maestro)
        db.session.commit()
        return redirect(url_for('maestros.index'))

    maestros = Maestros.query.all()
    return render_template("maestros/index.html", form=create_form, maestros=maestros)

@maestros_bp.route('/maestros/crear', methods=['GET', 'POST'])
def crear():
    create_form = forms.MaestroForm(request.form)
    if request.method == 'POST':
        maestro = Maestros()
        maestro.matricula = create_form.matricula.data
        maestro.nombre = create_form.nombre.data
        maestro.apellidos = create_form.apellidos.data
        maestro.especialidad = create_form.especialidad.data
        maestro.email = create_form.email.data
        db.session.add(maestro)
        db.session.commit()
        return redirect(url_for('maestros.index'))
    return render_template("maestros/crear.html", form=create_form)

@maestros_bp.route('/maestros/detalles/<matricula>')
def detalles(matricula):
    maestro = Maestros.query.filter_by(matricula=matricula).first()
    if maestro:
        return render_template(
            "maestros/detalles.html",
            matricula=maestro.matricula,
            nombre=maestro.nombre,
            apellidos=maestro.apellidos,
            especialidad=maestro.especialidad,
            email=maestro.email
        )
    else:
        return redirect(url_for('maestros.index'))

# modificar
@maestros_bp.route('/maestros/modificar/<matricula>', methods=['GET', 'POST'])
def modificar(matricula):
    maestro = Maestros.query.filter_by(matricula=matricula).first()
    if not maestro:
        return redirect(url_for('maestros.index'))

    create_form = forms.MaestroForm(request.form, obj=maestro)

    if request.method == 'POST':
        maestro.matricula = create_form.matricula.data
        maestro.nombre = create_form.nombre.data
        maestro.apellidos = create_form.apellidos.data
        maestro.especialidad = create_form.especialidad.data
        maestro.email = create_form.email.data
        db.session.commit()
        return redirect(url_for('maestros.index'))

    return render_template("maestros/modificar.html", form=create_form, matricula=matricula)


@maestros_bp.route('/maestros/eliminar/<matricula>', methods=['GET', 'POST'])
def eliminar(matricula):
    maestro = Maestros.query.filter_by(matricula=matricula).first()
    if not maestro:
        return redirect(url_for('maestros.index'))

    create_form = forms.MaestroForm(obj=maestro)

    if request.method == 'POST':
        db.session.delete(maestro)
        db.session.commit()
        return redirect(url_for('maestros.index'))

    return render_template("maestros/eliminar.html", form=create_form, matricula=matricula)

# @app.route("/Alumnos", methods=['GET','POST'] )
# def alumnos():
#     create_form = forms.UserForm(request.form)
#     if request.method=='POST':
#         alum = Alumnos()
#         alum.nombre = create_form.nombre.data
#         alum.apaterno = create_form.apaterno.data
#         alum.amaterno = create_form.amaterno.data
#         alum.telefono = create_form.telefono.data
#         alum.email = create_form.email.data
#         db.session.add(alum)
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template("alumnos.html", form=create_form)

@maestros_bp.route('/perfil/<matricula>')
def perfil(matricula):
    return f"Perfil del maestro: {matricula}"