from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.objectid import ObjectId


users = Flask(__name__)
users.config['MONGO_URI'] = 'mongodb://localhost/Mongo_Python_teste_1'
mongo = PyMongo(users)


# Rota De Post
@users.route('/teste_1', methods=['POST'])
def create_user():
    nome = request.json['nome']
    telefone = request.json['telefone']
    CEP = request.json['CEP']

    if nome and telefone and CEP:
        id = mongo.db.teste_1.insert({
            'nome': nome,
            'telefone': telefone,
            'CEP': CEP
        })
        response = {'id': str(id),
                    'nome': nome,
                    'telefone': telefone,
                    'CEP': CEP}
        return jsonify(response)
    else:
        return not_found()
    return {'message': 'received'}


# Rota de listagem de dados
@users.route('/teste_1', methods=['GET'])
def get_users():
    usuario = mongo.db.teste_1.find()
    response = json_util.dumps(usuario)
    return Response(response, mimetype='application/json')


# Rota para consultar um unico usuario
@users.route('/teste_1/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.teste_1. find_one({'_id': ObjectId(id)})
    response = json_util.dumps(user)
    return Response(response, mimetype='application/json')


# Rota para consulta de dados faltantes
@users.errorhandler(404)
def not_found(error=None):
    response = jsonify(
        message={
            'message': 'Resource not Found: ' + request.url,
            'status': 404
    })
    response.status_code = 404
    return response


# Rota para exclusão de dados
@users.route('/testes_1/<id>', methods=['DELETE'])
def delete(id):
    mongo.db.testes_1.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'User ' + id + 'usuario excluido com sucesso!'})
    return response


# Rota para atualização de dados
@users.route('/testes_1/<id>', methods=['PUT'])
def update_user(id):
    nome = request.json['nome']
    telefone = request.json['telefone']
    CEP = request.json['CEP']

    if nome and telefone and CEP:
        mongo.db.testes_1.update_one({'_id': ObjectId(id)}, {'$set': {
            'nome': nome,
            'telefone': telefone,
            'CEP': CEP
        }})
        response = jsonify({'message': 'User ' + id + ' Usuario atualizado!'})
        return response


if __name__ == "__main__":
    users.run(debug=True)