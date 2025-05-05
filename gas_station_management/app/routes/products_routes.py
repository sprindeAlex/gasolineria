from flask import Blueprint
from app.controllers.products_controller import ProductsController

products_routes = Blueprint('products', __name__)

@products_routes.route('/products', methods=['GET'])
def get_products():
    return ProductsController.get_all_products()

@products_routes.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    return ProductsController.get_product(product_id)

@products_routes.route('/products', methods=['POST'])
def create_product():
    return ProductsController.create_product()

@products_routes.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    return ProductsController.update_product(product_id)

@products_routes.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    return ProductsController.delete_product(product_id)