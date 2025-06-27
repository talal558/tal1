from django.test import TestCase
from products.models import Product

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='هاتف ذكي',
            description='هاتف ذكي بمواصفات عالية',
            price=2999.99,
            stock=50
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'هاتف ذكي')
        self.assertEqual(self.product.price, 2999.99)

    def test_product_str_method(self):
        self.assertEqual(str(self.product), self.product.name)

    def test_product_stock_is_positive(self):
        self.assertGreaterEqual(self.product.stock, 0)
