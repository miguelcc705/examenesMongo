from flask import Flask, request, jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#Crud para examenes

#traer un examen por id
@app.route("/examen/<code>", methods=['GET'])
def get_examen(code):
    con = db.get_connection()
    dbexam = con.examenes_medicos
    try:
        examenes = dbexam.Examenes
        response = app.response_class(
            response=dumps(examenes.find_one({'_id': ObjectId(code)})),
            status=200,
            mimetype='application/json'
        )
        return response
    finally:
        con.close()
        print("Connection closed")

#traer un examen por datos del paciente

@app.route("/examenbyid/<int:code>", methods=['GET'])
def get_examen_ID(code):
    con = db.get_connection()
    db_e = con.examenes_medicos

    try:
        examenes = db_e.Examenes
        pacientes = db_e.Paciente

        paciente = pacientes.find_one({'Documento': code})
        if paciente:
            paciente_id = paciente['_id']
            examenes_paciente = examenes.find({'id_paciente': paciente_id})
            examenes_list = [examen for examen in examenes_paciente]

            if examenes_list:
                response = app.response_class(
                    response=dumps(examenes_list),
                    status=200,
                    mimetype='application/json'
                )
                return response

        return 'No se encontraron exámenes para el paciente con documento de identidad {}'.format(code), 404

    finally:
        con.close()
        print("Connection closed")

@app.route("/examenbyemail/<code>", methods=['GET'])
def get_examen_email(code):
    con = db.get_connection()
    db_e = con.examenes_medicos

    try:
        examenes = db_e.Examenes
        pacientes = db_e.Paciente

        paciente = pacientes.find_one({'email': code})
        if paciente:
            paciente_id = paciente['_id']
            examenes_paciente = examenes.find({'id_paciente': paciente_id})
            examenes_list = [examen for examen in examenes_paciente]

            if examenes_list:
                response = app.response_class(
                    response=dumps(examenes_list),
                    status=200,
                    mimetype='application/json'
                )
                return response

        return 'No se encontraron exámenes para el paciente con email {}'.format(code), 404

    finally:
        con.close()
        print("Connection closed")


#traer todos los examenes
@app.route("/examenes", methods=['GET'])
def get_examenes():
    con = db.get_connection()
    dbexamenes = con.examenes_medicos
    try:
        examenes = dbexamenes.Examenes
        response = app.response_class(
            response=dumps(
                examenes.find()
            ),
            status=200,
            mimetype='application/json'
        )
        return response
    finally:
        con.close()
        print("Connection closed")

#Crear un examen
@app.route("/examenes", methods=['POST'])
def create_examen():
    data = request.get_json()
    con = db.get_connection()
    dbexamenes = con.examenes_medicos 
    try:
        examenes = dbexamenes.Examenes
        examenes.insert_one(data)
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

#Actualizar un examen
@app.route("/examenes/<code>", methods=['PUT'])
def update_examen(code):
    data = request.get_json()
    con = db.get_connection()
    dbexamenes = con.examenes_medicos 
    try:
        examenes = dbexamenes.Examenes
        examenes.replace_one(
            {'_id': ObjectId(code)},
            data, True
        )
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

#Borrar un examen
@app.route("/examenes/<code>", methods=['DELETE'])
def delete_examen(code):
    con = db.get_connection()
    dbexamenes = con.examenes_medicos
    try:
        examenes = dbexamenes.Examenes
        examenes.delete_one({'_id': ObjectId(code)})
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")





#Crud para pacientes

#traer un paciente por id
@app.route("/paciente/<code>", methods=['GET'])
def get_paciente(code):
    con = db.get_connection()
    dbexam = con.examenes_medicos
    try:
        pacientes = dbexam.Paciente
        response = app.response_class(
            response=dumps(pacientes.find_one({'_id': ObjectId(code)})),
            status=200,
            mimetype='application/json'
        )
        return response
    finally:
        con.close()
        print("Connection closed")

#traer todos los pacientes
@app.route("/pacientes", methods=['GET'])
def get_pacientes():
    con = db.get_connection()
    dbexamenes = con.examenes_medicos
    try:
        pacientes = dbexamenes.Paciente
        response = app.response_class(
            response=dumps(
                pacientes.find()
            ),
            status=200,
            mimetype='application/json'
        )
        return response
    finally:
        con.close()
        print("Connection closed")

#Crear un paciente
@app.route("/paciente", methods=['POST'])
def create_paciente():
    data = request.get_json()
    con = db.get_connection()
    dbexamenes = con.examenes_medicos
    try:
        pacientes = dbexamenes.Paciente
        pacientes.insert_one(data)
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

#Actualizar un paciente
@app.route("/pacientes/<code>", methods=['PUT'])
def update_paciente(code):
    data = request.get_json()
    con = db.get_connection()
    dbexamenes = con.examenes_medicos
    try:
        pacientes = dbexamenes.Paciente
        pacientes.replace_one(
            {'_id': ObjectId(code)},
            data, True
        )
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

#Borrar un examen
@app.route("/pacientes/<code>", methods=['DELETE'])
def delete_paciente(code):
    con = db.get_connection()
    dbexamenes = con.examenes_medicos
    try:
        pacientes = dbexamenes.Paciente
        pacientes.delete_one({'_id': ObjectId(code)})
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")