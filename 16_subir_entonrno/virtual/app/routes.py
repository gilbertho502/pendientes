from flask import render_template,make_response,jsonify,request
from app import app,db
from app.models import Grupos, Alumnos
from app.serializer import grupos_schema,grupo_schema, alumno_schema, alumnos_schema


@app.route('/')
def index():
    template_name="index.html"
    grupos=Grupos.query.all()
    return render_template(template_name,grupos=grupos)


#todo crear el endpoint para traer todas los grupos
#todo en formato JSON

#listar grupos

@app.route("/listar_grupos",methods=["GET"])
def listar_grupos():
    #todo seleccionado todos los objetos de la clase grupos
    grupos=Grupos.query.all()
    #todo serializando y seleccionado los atributos a cast en json
    #todo dump nos permite serializar los objetos de PYTHON 
    result=grupos_schema.dump(grupos)
    
    #todo creando el documento de salida
    data={
        'message':'Todas mis grupos',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))

#Detalle de grupo

@app.route("/detalle_grupo/<id>",methods=["GET"])
def detalle_grupo(id):
    #todo para seleccionar solo un objeto por id
    grupo=Grupos.query.get(id)
    if grupo:
        #todo dump permite serializar los objetos en PYTHON
        #todo como por ejemplo convertir un STR en json
        result=grupo_schema.dump(grupo)        
        data= {
        'message':'1',
        'status':200,
        'data':result
            }
    else:
        data = {
            'message':'0',
            'status':200,
        }
    return make_response(jsonify(data))

#agregar grupo

@app.route("/add_grupo",methods=["POST"])
def add_grupo():
    #todo request tomar los parametros qe se insertarn en
    #todo la tablas
    codgrupo = request.json['codgrupo']
    nombre_grupo=request.json['nombre_grupo']
    descripcion_grupo = reques.json['descripcion_grupo']
    estado=request.json['estado']
    
    new_grupo = Grupos(codgrupo, nombre_grupo,descripcion_grupo,estado)
    #todo se guarda el objeto en la session del usuario
    db.session.add(new_grupo)
    #todo se guarda fisicamente en la tabla
    db.session.commit()
    #todo esto permitira que el front vea cual es el registro
    #todo que se inserto
    result=grupo_schema.dump(new_grupo)
    
    data = {
        'message':'Se Agrego con exito',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))

#eliminar grupo

@app.route("/delete_grupo/<id>",methods=["DELETE"])
def delete_grupo(id):
    #todo para seleccionar solo un objeto por id
    grupo=Grupos.query.get(id)
    if grupo:
        
        #todo elimino el objeto de la session y la tabla
        db.session.delete(grupo)
        db.session.commit()
        
        data= {
            'message':'1',
            'status':200,
            }
    else:
        data = {
            'message':'0',
            'status':200,
        }
    return make_response(jsonify(data))

#editar grupo


@app.route("/edit_grupo/<int:id>",methods=["PUT"])
def edit_grupo(id):
    grupo=Grupos.query.get(id)
    if grupo:
        nombre_grupo=request.json['nombre_grupo']
        estado=request.json['estado']
        #todo pasalonde los valores a actualizar
        grupo.nombre_grupo=nombre_grupo
        grupo.estado=estado
        
        db.session.commit()
        result=grupo_schema.dump(grupo)        
        data= {
            'message':'1',
            'status':200,
            'data':result
                }
    else:
        data = {
            'message':'0',
            'status':200,
        }   
    return make_response(jsonify(data))
    

#LISTAR TODOS LOS ALUMNOS
   
@app.route("/listar_alumnos",methods=["GET"])
def listar_alumnos():
    alumnos=Alumnos.query.all()
    result=alumnos_schema.dump(alumnos)
    data={
        'message':'Todas mis Alumnos :)',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))


#Detallar alumno

@app.route("/detalle_alumno/<id>",methods=["GET"])
def detalle_alumno(id):
    alumno=Alumnos.query.get(id)
    if alumno:

        result=alumno_schema.dump(alumno)        
        data= {
        'message':'1',
        'status':200,
        'data':result
            }
    else:
        data = {
            'message':'0',
            'status':200,
        }
    return make_response(jsonify(data))

#Agregar alumno

@app.route("/add_alumno",methods=["POST"])
def add_alumno():

    codalu = request.json['codalu']
    nombre_alumno = request.json['nombre_alumno']
    apellido_alumno = request.json['apellido_alumno']
    edad_alumno = request.json['edad_alumno']
    fechanac_alumno = request.json['fechanac_alumno']
    ciudad = request.json['ciudad']
    estado = request.json['estado']
    codgrupo = request.json['codgrupo']
    
    new_alumno = Alumnos(codalu, nombre_alumno, apellido_alumno, edad_alumno, fechanac_alumno, ciudad, estado, codgrupo)
    db.session.add(new_alumno)
    db.session.commit()
    result=grupo_schema.dump(new_alumno)
    
    data = {
        'message':'Se Agrego con exito',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))

