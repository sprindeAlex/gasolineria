from app.models.product import Product
from app.config.database import db_session

class ProductService:
    @staticmethod
    def create_product(name, price, iva):
        new_product = Product(name=name, price=price, iva=iva)
        db_session.add(new_product)
        db_session.commit()
        return new_product

    @staticmethod
    def get_product(product_id):
        return db_session.query(Product).filter(Product.id == product_id).first()

    @staticmethod
    def update_product(product_id, name, price, iva):
        product = db_session.query(Product).filter(Product.id == product_id).first()
        if product:
            product.name = name
            product.price = price
            product.iva = iva
            db_session.commit()
        return product

    @staticmethod
    def delete_product(product_id):
        product = db_session.query(Product).filter(Product.id == product_id).first()
        if product:
            db_session.delete(product)
            db_session.commit()
        return product is not None

    @staticmethod
    def get_all_products():
        return db_session.query(Product).all()