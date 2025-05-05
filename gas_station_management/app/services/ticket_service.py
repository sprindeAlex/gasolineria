from app.models.ticket import Ticket
from app.models.user import User
from app.models.product import Product

class TicketService:
    def __init__(self, db_session):
        self.db_session = db_session

    def create_ticket(self, ticket_data):
        ticket = Ticket(**ticket_data)
        self.db_session.add(ticket)
        self.db_session.commit()
        return ticket

    def get_ticket(self, ticket_id):
        return self.db_session.query(Ticket).filter_by(id=ticket_id).first()

    def update_ticket(self, ticket_id, ticket_data):
        ticket = self.get_ticket(ticket_id)
        if ticket:
            for key, value in ticket_data.items():
                setattr(ticket, key, value)
            self.db_session.commit()
            return ticket
        return None

    def delete_ticket(self, ticket_id):
        ticket = self.get_ticket(ticket_id)
        if ticket:
            self.db_session.delete(ticket)
            self.db_session.commit()
            return True
        return False

    def get_all_tickets(self):
        return self.db_session.query(Ticket).all()