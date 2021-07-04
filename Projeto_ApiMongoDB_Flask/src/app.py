from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.objectid import ObjectId

app = Flask(__name__)
# conectando com o banco e dado um nomo para o banco
app.config["MONGO_URI"] = 'mongodb://localhost/PythonMongoDB'
# guanrdando os dados do banco em uma variável
mongo = PyMongo(app)


# Rota de post >>> OK
@app.route('/users', methods=['POST'])
def create_user():
    print(request.json)
    # Enviando dados para mongoDB
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    # Validando os dados e verificando se foi enviado
    if username and password and email:
        #Escondendo a o valor da password com generate_password_hash()
        hashed_password = generate_password_hash(password)
        id = mongo.db.users.insert({'username': username,
                                    'email': email,
                                    'password': hashed_password})
        response = {'id': str(id),
                    'username': username,
                    'email': email,
                    'password': hashed_password
                    }
        return jsonify(response)
    else:
        return not_found()
    return {'message': 'received'}


# Rota para listagem de dados >>> OK
@app.route('/users', methods=["GET"])
def get_users():
    """Usando função do mongo pra listar dados find()"""
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    return Response(response, mimetype='application/json')


# Rota para consultar somente um ID de usuário
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(user)
    return Response(response, mimetype='application/json')


# Rota de tratamento no caso de dados faltantes >>> OK
@app.errorhandler(404)
def not_found(error=None):
    """Tratamento de dados faltantes"""
    response = jsonify(
        message={
            'message': 'Resource Not Found: ' + request.url,
            'status': 404
        })
    response.status_code = 404
    return response


# Rota para deleção de dados
@app.route('/users/<id>', methods=['DELETE'])
def delete(id):
    """Excluindo usuários do banco"""
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'User ' + id + ' Usuário eliminado com Sucesso!'})
    return response


# Rota para atualizar usuarios no banco MongoDB
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    if username and email and password:
        hashed_password = generate_password_hash(password)
        mongo.db.users.update_one({'_id': ObjectId(id)}, {'$set': {
            'username': username,
            'password': hashed_password,
            'email': email
        }})
        response = jsonify({'message': 'User ' + id + 'Usuário Atualizado com Sucesso!'})
        return response


if __name__ == "__main__":
    app.run(debug=True)