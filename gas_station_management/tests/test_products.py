import unittest
from app.models.product import Product

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = Product(name="Test Product", price=10.0, iva=0.21)

    def test_product_creation(self):
        self.assertIsInstance(self.product, Product)
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, 10.0)
        self.assertEqual(self.product.iva, 0.21)

    def test_product_price_with_iva(self):
        expected_price_with_iva = self.product.price * (1 + self.product.iva)
        self.assertEqual(self.product.get_price_with_iva(), expected_price_with_iva)

    def test_product_str(self):
        self.assertEqual(str(self.product), "Test Product - Price: 10.0")