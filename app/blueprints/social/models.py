from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(120), nullable=True)
    username = db.Column(db.String(64), unique=True, nullable=True)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    cars = db.relationship('Car', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'User: {self.username}'
    
    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password) 

    def commit(self):
        db.session.add(self)   
        db.session.commit()

class Car(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    make= db.Column(db.String(50),nullable=True)
    model=db.Column(db.String(50),nullable=True)
    color=db.Column(db.String(50),nullable=True)
    year=db.Column(db.Integer,nullable=True)
    price=db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Car make: {self.make} model: {self.model} color: {self.color} year: {self.year} price: {self.price}'

    def commit(self):
        db.session.add(self)
        db.session.commit()

 