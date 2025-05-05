class Ticket:
    def __init__(self, ticket_id, customer_id, product_id, quantity, total_price, date):
        self.ticket_id = ticket_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_price = total_price
        self.date = date

    def calculate_total(self, price_per_unit):
        self.total_price = price_per_unit * self.quantity

    def get_ticket_details(self):
        return {
            "ticket_id": self.ticket_id,
            "customer_id": self.customer_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "total_price": self.total_price,
            "date": self.date
        }