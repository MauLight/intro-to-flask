from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key= True)

    username = db.Column(db.String(200), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable= False)
    lastname = db.Column(db.String(50), nullable= False)
    password = db.Column(db.String(50), nullable= False)
    date_of_birth = db.Column(db.String(50))
    email = db.Column(db.String(50), nullable= False, unique = True)
    verified = db.Column(db.Boolean(), default = True)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'lastname': self.lastname,
            'password' : self.password,
            'date_of_birth': self.date_of_birth,
            'email': self.email,
            'verified': self.verified
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

