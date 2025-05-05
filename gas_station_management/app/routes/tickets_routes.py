from flask import Blueprint, request, jsonify
from app.controllers.tickets_controller import TicketsController

tickets_routes = Blueprint('tickets', __name__)

@tickets_routes.route('/tickets', methods=['GET'])
def get_tickets():
    return TicketsController.get_all_tickets()

@tickets_routes.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    return TicketsController.get_ticket(ticket_id)

@tickets_routes.route('/tickets', methods=['POST'])
def create_ticket():
    ticket_data = request.json
    return TicketsController.create_ticket(ticket_data)

@tickets_routes.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    ticket_data = request.json
    return TicketsController.update_ticket(ticket_id, ticket_data)

@tickets_routes.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    return TicketsController.delete_ticket(ticket_id)