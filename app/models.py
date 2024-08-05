from .database import db

class Product(db.Model):
    __tablename__ = 'products'
    sku = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    link_produto = db.Column(db.String(255), nullable=False) 

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    telefone = db.Column(db.String(20), nullable=False)

class Sessions(db.Model):
    __tablename__ = 'sessions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    session_id = db.Column(db.String(100), nullable=False)
    chat_message_history = db.Column(db.Text, nullable=False)