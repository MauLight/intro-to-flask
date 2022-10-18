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

@app.route('/api/users', methods= ['GET'])
def list_users():
    users = User.query.all()

if __name__ == '__main__':
    app.run()