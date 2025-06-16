from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
db = SQLAlchemy()


class User(db.Model):#se define la entidad(tabla),que representa al Usuario
    __tablename__="user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)#es la primary key,por ende no se repite,es un numero y es unico  
    full_name: Mapped[str] = mapped_column(String, nullable=False)#es un string, que no puede ser nulo
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)#string,que es unico,y tampoco puede ser nulo
    password: Mapped[str] = mapped_column(String, nullable=False)#string,que no puede ser nulo


    def serialize(self):#se agrega una función para mostrar la información de un usuario
        return{
            "id":self.id,
            "full_name":self.full_name,
            "email":self.email
        }
    def hash_password(self,password):#se utiliza werkzeug para encriptar la contraseña del usuario
        self.password=generate_password_hash(password)
        return self.password