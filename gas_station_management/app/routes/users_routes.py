from flask import Blueprint, request, jsonify
from app.controllers.users_controller import UsersController

users_routes = Blueprint('users', __name__)

@users_routes.route('/users', methods=['GET'])
def get_users():
    return UsersController.get_all_users()

@users_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return UsersController.get_user(user_id)

@users_routes.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    return UsersController.create_user(user_data)

@users_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.json
    return UsersController.update_user(user_id, user_data)

@users_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return UsersController.delete_user(user_id)