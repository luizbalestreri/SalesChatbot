import uuid
from flask import Blueprint, request, jsonify
from .models import Product, Usuario
from .database import db
from app.chatbot import processar_mensagem

main = Blueprint('main', __name__)

@main.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data['message'] # Get history if provided, otherwise use empty list
    bot_response = processar_mensagem(message)
    return jsonify({"response": bot_response})

@main.route('/categories', methods=['GET'])
def get_categories():
    categories = db.session.query(Product.category).distinct().all()
    categories = [category[0] for category in categories]
    return jsonify(categories)

@main.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    products_list = [{'sku': p.sku, 'name': p.name, 'quantity': p.quantity, 'description': p.description, 'price': p.price, 'category': p.category} for p in products]
    return jsonify(products_list)

@main.route('/products/<sku>/description', methods=['GET'])
def get_product_description(sku):
    product = Product.query.get(sku)
    if product:
        return jsonify({'sku': product.sku, 'description': product.description})
    else:
        return jsonify({'error': 'Product not found'}), 404

@main.route('/products/<sku>/price', methods=['GET'])
def get_product_price(sku):
    product = Product.query.get(sku)
    if product:
        return jsonify({'sku': product.sku, 'price': product.price})
    else:
        return jsonify({'error': 'Product not found'}), 404

@main.route('/products/<sku>/quantity', methods=['GET'])
def get_product_quantity(sku):
    product = Product.query.get(sku)
    if product:
        return jsonify({'sku': product.sku, 'quantity': product.quantity})
    else:
        return jsonify({'error': 'Product not found'}), 404
    
@main.route('/products/<sku>/link', methods=['GET'])
def get_product_link(sku):
    product = Product.query.get(sku)
    if product:
        return jsonify({'sku': product.sku, 'link_produto': product.link_produto})
    else:
        return jsonify({'error': 'Product not found'}), 404

@main.route('/usuarios', methods=['POST'])
def add_usuario():
    data = request.json
    nome = data.get('nome')
    email = data.get('email')
    telefone = data.get('telefone')
    if not nome or not email or not telefone:
        return jsonify({'error': 'Missing required fields'}), 400
    
    usuario = Usuario(nome=nome, email=email, telefone=telefone)
    db.session.add(usuario)
    db.session.commit()
    return jsonify({'message': 'User added successfully', 'user_id': usuario.id}), 201

@main.route('/usuarios/<email>', methods=['GET'])
def get_usuario(email):
    usuario = Usuario.query.filter_by(email=email).first()
    if usuario:
        return jsonify({'id': usuario.id, 'nome': usuario.nome, 'email': usuario.email, 'telefone': usuario.telefone})
    else:
        return jsonify({'error': 'User not found'}), 404