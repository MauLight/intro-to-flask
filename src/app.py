from flask import Flask, request, jsonify, json
from flask_migrate import Migrate
from models import db, User

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 'dialect+driver://<user>:<pass>@<host>:<port>/<dbname>'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Mau_Light:motmot19842016.@localhost:3306/Test'

db.init_app(app) # vinculo entre mi app y mis modelos de la base de datos
Migrate(app, db) # db init, db migrate, db upgrade || db downgrade

@app.route('/', methods= ['GET'])
def main():
    return 'REST API'

@app.route('/api/users', methods=['GET']) 
def list_users():
    users = User.query.all()
    users = list(map(lambda user: user.serialize(), users))
    return jsonify(users) 

@app.route('/api/users', methods = ['POST'])
def save_user():
    username = request.json.get('username')
    name = request.json.get('name')
    lastname = request.json.get('lastname')
    password = request.json.get('password')
    birthdate = request.json.get('date_of_birth')
    email = request.json.get('email')
    verified = request.json.get('verified')

    user = User()
    user.username = username
    user.name = name
    user.lastname = lastname
    user.password = password
    user.birthdate = birthdate
    user.email = email
    user.verified = verified

    user.save()
    return jsonify(user.serialize()), 201

@app.route('/api/users/<int:id>', methods = ['PUT'])
def update_user(id):
    username = request.json.get('username')
    name = request.json.get('name')
    lastname = request.json.get('lastname')
    password = request.json.get('password')
    birthdate = request.json.get('date_of_birth')
    email = request.json.get('email')
    verified = request.json.get('verified')

    user = User.query.get(id)
    user.username = username
    user.name = name
    user.lastname = lastname
    user.password = password
    user.birthdate = birthdate
    user.email = email
    user.verified = verified

    user.update()
    return jsonify(user.serialize()), 200

@app.route('/api/users/search', methods = ['GET'])
def search_users():
    search = request.args
    users = User.query.filter(User.username.ilike('%'+search['username']+'%'))
    users = list(map(lambda user: user.serialize(), users))

    return jsonify(users), 200


if __name__ == '__main__':
    app.run()