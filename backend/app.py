from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/register', methods=['POST'])
def register_user():
    # valida que en el body venga un json
    if request.content_type != 'application/json':
        return jsonify({'error': 'Debe enviarse un JSON en el body'}), 400
    
    print(request.json)
    
    
    return jsonify({'message':'Registro realizado con exito'}), 201

