#IMPORTS NATIVOS DE PYTHON.
import os
from datetime import datetime, timedelta

#IMPORTS NATIVOS DEL FRAMEWORK
from flask import (
    render_template, 
    redirect, 
    request, 
    url_for, 
    jsonify
)
from flask_jwt_extended import ( 
    jwt_required, 
    create_access_token, 
    get_jwt_identity, 
    get_jwt)
from werkzeug.security import( 
    generate_password_hash, 
    check_password_hash
)
#IMPORTS PROPIOS
from app import app, db, jwt
from app.models.models import *
from app.schemas.schemas import EmpleadoSchema

@app.route("/empleados")

def get_all_empleados():
    #
    
    # Obtener todos los empleados paginados
    page = request.args.get('page', 1, type=int)
    can = request.args.get('can', 1000, type=int)
    empleados = db.session.query(Empleado).paginate(
        page=page, per_page=can
    )
        
    return jsonify(
        {
            "results": EmpleadoSchema().dump(empleados.items, many=True)
        }
    )



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar_empleado', methods=['POST'])
def nuevo_empleado():
    if request.method == 'POST':
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        email = request.form["email"]
        telefono = request.form["telefono"]
        fecha_cont= request.form["fecha_contratacion"]
        departamento_id= request.form["departamento_id"]
        puesto_id= request.form["puesto_id"]

        nuevo_empleado = Empleado(nombre=nombre,
                                  apellido=apellido,
                                  email=email,
                                  telefono=telefono,
                                  fecha_contratacion=fecha_cont,
                                  departamento_id=departamento_id,
                                  puesto_id=puesto_id
                                  )

        # Guardar en la base de datos
        db.session.add(nuevo_empleado)
        db.session.commit()

        return redirect(url_for('index'))

@app.route('/borrar_empleado/<id>')
def borrar_empleado(id):
    empleado = Empleado.query.get(id)
    db.session.delete(empleado)
    db.session.commit()
    return redirect(url_for('index'))
