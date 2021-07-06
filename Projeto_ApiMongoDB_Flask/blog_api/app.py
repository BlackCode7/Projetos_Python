from flask import Flask, request, Response, jsonify
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId


app = Flask(__name__)

# Conectando com o banco
app.config['MONGO_URI'] = 'mongodb://localhost/MongoDB_BLOG'
mongo = PyMongo(app)


@app.route('/blogs', methods=['POST'])
def create_user():
    nome = request.json['nome']
    comentario = request.json['comentario']
    data = request.json['data']

    if data and comentario and data:
        id = mongo.db.Blog.insert({
            'nome': nome,
            'comentario': comentario,
            'data': data
        })
        response = {'id': str(id),
                    'nome': nome,
                    'comentario': comentario,
                    'data': data}
        return jsonify(response)
    else:
        return not_found()

    return {'message': 'received'}


# Rota de listagem de tweets
@app.route('/blogs', methods=['GET'])
def get_users():
    blog = mongo.db.Blog.find()
    response = json_util.dumps(blog)
    return Response(response, mimetype='application/json')


# Rota para consultar um unico tweet
@app.route('/blogs/<id>', methods=['GET'])
def get_user(id):
    blog = mongo.db.Blog. find_one({'_id': ObjectId(id)})
    response = json_util.dumps(blog)
    return Response(response, mimetype='application/json')


# Rota para tratamento de dados faltantes
@app.errorhandler(404)
def not_found(error=None):
    response = jsonify(
        message={
            'message': "Resource Not Found: " + request.url,
            'status': 404
        })
    response.status_code = 404
    return response


# Rota para deleção de dados
@app.route('/blogs/<id>', methods=['DELETE'])
def delete_blog(id):
    """Excluindo usuários do banco"""
    mongo.db.Blog.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'Tweet ' + id + ' Twwet eliminado com Sucesso!'})
    return response


# Rota para atualizar usuarios no banco MongoDB
@app.route('/blogs/<id>', methods=['PUT'])
def update_blog(id):
    nome = request.json['nome']
    comentario = request.json['comentario']
    data = request.json['data']

    if nome and comentario and data:
        mongo.db.Blog.update_one({'_id': ObjectId(id)}, {'$set': {
            'nome': nome,
            'comentario': comentario,
            'data': data
        }})
        response = jsonify({'message': 'Tweet ' + id + 'Tweet Atualizado com Sucesso!'})
        return response


if __name__ == '__main__':
    app.run(debug=True)