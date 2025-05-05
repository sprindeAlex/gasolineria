import unittest
from app.models.ticket import Ticket

class TestTicket(unittest.TestCase):

    def setUp(self):
        self.ticket = Ticket(id=1, client_id=1, product_id=1, quantity=2, total_price=20.0)

    def test_ticket_creation(self):
        self.assertEqual(self.ticket.id, 1)
        self.assertEqual(self.ticket.client_id, 1)
        self.assertEqual(self.ticket.product_id, 1)
        self.assertEqual(self.ticket.quantity, 2)
        self.assertEqual(self.ticket.total_price, 20.0)

    def test_ticket_total_price_calculation(self):
        self.ticket.quantity = 3
        self.ticket.total_price = self.ticket.quantity * 10.0  # Assuming price per product is 10.0
        self.assertEqual(self.ticket.total_price, 30.0)

if __name__ == '__main__':
    unittest.main()