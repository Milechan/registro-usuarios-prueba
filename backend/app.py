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

@app.route("/register", methods=["POST"])#ruta para registro
def register_user():
    # valida que en el body venga un json
    if request.content_type != "application/json":
        return jsonify({"error": "Debe enviarse un JSON en el body"}), 400
    
    print(request.json)#imprimir un json
    body = request.json
    if body["full_name"] is None or body["full_name"] == "":
        return jsonify({"error":"se necesita enviar un nombre completo"}),400#validacion de que venga el nombre completo
    if body["email"] is None or body["email"] == "":
        return jsonify({"error":"se necesita que se envie un correo"}),400#validacion de que se envie un correo
    if body["password"] is None or body["password"] == "":
        return jsonify({"error":"se necesita que envie una contraseña"}),400#validacion que se envie una contraseña
    
    email_regex = re.compile(r"^[\w\-\.]+@([\w\-]+\.)+[\w\-]{2,4}$")
    if re.match(email_regex,body["email"]) is None:
        return jsonify({"error":"el correo no tiene un formato valido"}),400#se valida con una expresion regular(un patron) que el correo tenga un formato valido
    if len(body["password"])<6:
        return jsonify({"error":"la contraseña debe tener como minimo 6 caracteres"}),400#validar el minimo de caracterres que debe tener la contraseña
    user_exist = db.session.query(User).filter_by(email=body["email"]).one_or_none()
    if user_exist is not None:
        return jsonify({"error":"ya existe un usuario con ese correo"}),409#validar si es que el usuario ya existe
    
    #se crea el nuevo usuario,con la información que viene en el body
    new_user = User()
    new_user.full_name=body["full_name"]
    new_user.email=body["email"]
    new_user.password=new_user.hash_password(body["password"])#aqui se hashea la contraseña (se encripta)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message":"Registro realizado con exito"}), 201#se envia la respuesta final ,una vez que se arealiza el registro

@app.route("/listusers",methods=["GET"])#ruta para obtener la lista de usuarios
def get_all_users():
    user_list=db.session.query(User).all()
    return jsonify({"users":[user.serialize() for user in user_list]}),200