
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS
import json
from bson import json_util

app = Flask(__name__)
CORS(app)

import pymongo

#conectarmen con mongodb
database = pymongo.MongoClient()
#conectarme con el servidor local 
database = pymongo.MongoClient('mongodb://localhost:27017/')
#se conecta la bd cargamos a la tabla alumnos
alumnos = database['cargamos']['alumnos']

@app.route('/api/alumnos',methods=['GET'])
def mostrar_alumnos():
    response = []
    for docu in alumnos.find():
        response.append(docu)

    return json.dumps(response, default=json_util.default)

@app.route('/api/register', methods= ['pOST'])
def registar():
    data = request.get_json()
    obj = {
        'name': data['name'],
        'apellido': data['apellido'],
        'edad': data['edad']
    }
    res = alumnos.insert_one(obj)

    return jsonify({
        'message': 'alumno registrado correctamente',
        'status': 200
    })



@app.route('/api/alumnos/<name>',methods=['GET'])
def mostrar_alumno(name):
    alumno = alumnos.find_one({'name':'name'})
    return json.dumps(alumno, default=json_util.default)



app.run(debug=True, port=5000)
