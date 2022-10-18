from flask import Flask, jsonify, request, json     

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'

@app.route('/', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def first():
    return 'Hello there world!'

@app.route('/api/users', methods = ['GET'])
def users():
    users = [{'id': 1, 'name': 'Mau'}]

    return jsonify(users), 200

@app.route('/api/users/<int:id>', methods = ['GET', 'POST'])
def users_by_id(id):
    if request.method == 'GET':
        users = [{'id': 1, 'name': 'Mau'}]
        query = request.query_string
        print(query)
        user = list(map(lambda user: user if user['id'] == id else None, users))
        return jsonify(user[0]), 200
    
    if request.method == 'POST':
        data = json.loads(request.data)
        name = request.json.get("name")
        print(data["name"])
        print(name) 
        return jsonify(data)
 
if __name__ == '__main__':
    app.run() 