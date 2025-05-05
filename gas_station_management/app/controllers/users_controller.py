from flask import Blueprint, request, jsonify
from app.models.user import User
from app.services.user_service import UserService

users_controller = Blueprint('users_controller', __name__)
user_service = UserService()

@users_controller.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    return jsonify(users), 200

@users_controller.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'message': 'User not found'}), 404

@users_controller.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = user_service.create_user(data)
    return jsonify(user), 201

@users_controller.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = user_service.update_user(user_id, data)
    if user:
        return jsonify(user), 200
    return jsonify({'message': 'User not found'}), 404

@users_controller.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    success = user_service.delete_user(user_id)
    if success:
        return jsonify({'message': 'User deleted successfully'}), 204
    return jsonify({'message': 'User not found'}), 404