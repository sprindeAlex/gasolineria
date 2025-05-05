from flask import Blueprint, request, jsonify
from app.models.product import Product
from app.services.product_service import ProductService

products_controller = Blueprint('products_controller', __name__)
product_service = ProductService()

@products_controller.route('/products', methods=['GET'])
def get_products():
    products = product_service.get_all_products()
    return jsonify(products), 200

@products_controller.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = product_service.get_product_by_id(product_id)
    if product:
        return jsonify(product), 200
    return jsonify({'message': 'Product not found'}), 404

@products_controller.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = product_service.create_product(data)
    return jsonify(new_product), 201

@products_controller.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    updated_product = product_service.update_product(product_id, data)
    if updated_product:
        return jsonify(updated_product), 200
    return jsonify({'message': 'Product not found'}), 404

@products_controller.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    success = product_service.delete_product(product_id)
    if success:
        return jsonify({'message': 'Product deleted'}), 200
    return jsonify({'message': 'Product not found'}), 404