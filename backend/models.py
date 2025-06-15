from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
db = SQLAlchemy()


class User(db.Model):
    __tablename__="user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    full_name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)


    def serialize(self):
        return{
            "id":self.id,
            "full_name":self.full_name,
            "email":self.email
        }
    def hash_password(self,password):
        self.password=generate_password_hash(password)
        return self.password