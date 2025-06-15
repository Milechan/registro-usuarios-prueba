from app import db



class User(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    full_name=db.Column(db.String(80),nullable=False)
    email=db.Column(db.String(150),nullable=False,unique=True)
    password=db.Column(db.String(200),nullable=False)
    def serialize(self):
        return{
            "id":self.id,
            "full_name":self.full_name,
            "email":self.email
        }