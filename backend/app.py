from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from models import db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
CORS(app)
db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def hello_world():
    return "<p></p>"

@app.route("/register", methods=["POST"])
def register_user():
    # valida que en el body venga un json
    if request.content_type != "application/json":
        return jsonify({"error": "Debe enviarse un JSON en el body"}), 400
    
    print(request.json)
    
    
    return jsonify({"message":"Registro realizado con exito"}), 201

@app.route("/listusers",methods=["GET"])
def get_all_users():
    return jsonify({"users":[]}),200