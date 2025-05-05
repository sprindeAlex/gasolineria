from flask import Blueprint, request, jsonify
from app.services.ticket_service import TicketService

tickets_controller = Blueprint('tickets_controller', __name__)
ticket_service = TicketService()

@tickets_controller.route('/tickets', methods=['GET'])
def get_tickets():
    tickets = ticket_service.get_all_tickets()
    return jsonify(tickets), 200

@tickets_controller.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    ticket = ticket_service.get_ticket_by_id(ticket_id)
    if ticket:
        return jsonify(ticket), 200
    return jsonify({'message': 'Ticket not found'}), 404

@tickets_controller.route('/tickets', methods=['POST'])
def create_ticket():
    data = request.get_json()
    new_ticket = ticket_service.create_ticket(data)
    return jsonify(new_ticket), 201

@tickets_controller.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    data = request.get_json()
    updated_ticket = ticket_service.update_ticket(ticket_id, data)
    if updated_ticket:
        return jsonify(updated_ticket), 200
    return jsonify({'message': 'Ticket not found'}), 404

@tickets_controller.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    success = ticket_service.delete_ticket(ticket_id)
    if success:
        return jsonify({'message': 'Ticket deleted successfully'}), 200
    return jsonify({'message': 'Ticket not found'}), 404