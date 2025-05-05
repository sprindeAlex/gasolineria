class Product:
    def __init__(self, id, name, price, iva, modified):
        self.id = id
        self.name = name
        self.price = price
        self.iva = iva
        self.modified = modified

    def get_product_info(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "iva": self.iva,
            "modified": self.modified
        }

    def update_product(self, name=None, price=None, iva=None):
        if name is not None:
            self.name = name
        if price is not None:
            self.price = price
        if iva is not None:
            self.iva = iva

    def delete_product(self):
        # Logic to delete the product from the database
        pass