from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/registro', methods=['POST'])
def registro_usuario():
    # valida que en el body venga un json
    if request.content_type != 'application/json':
        return jsonify({'error': 'Debe enviarse un JSON en el body'}), 400
    
    print(request.json)
    
    
    return jsonify({'message':'Registro realizado con exito'}), 201

