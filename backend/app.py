from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from models import db , User
import re
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
    body = request.json
    if body.full_name is None or body.full_name == "":
        return jsonify({"error":"se necesita enviar un nombre completo"}),400
    if body.email is None or body.email == "":
        return jsonify({"error":"se necesita que se envie un correo"}),400
    if body.password is None or body.password == "":
        return jsonify({"error":"se necesita que envie una contraseña"}),400
    
    email_regex="^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$"
    if re.search(email_regex,body.email) is None:
        return jsonify({"error":"el correo no tiene un formato valido"}),400
    if len(body.password)<6:
        return jsonify({"error":"la contraseña debe tener como minimo 6 caracteres"}),400
    user_exist = db.session.query(User).filter_by(email=body.email).one_or_none()
    if user_exist is not None:
        return jsonify({"error":"ya existe un usuario con ese correo"}),409

    new_user = User()
    new_user.full_name=body.full_name
    new_user.email=body.email
    new_user.password=new_user.hash_password(body.password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message":"Registro realizado con exito"}), 201

@app.route("/listusers",methods=["GET"])
def get_all_users():
    user_list=db.session.query(User).all()
    return jsonify({"users":[user.serialize() for user in user_list]}),200