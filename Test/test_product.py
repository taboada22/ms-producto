import unittest
#from flask import jsonify
from app.Services.product import ProductService
from . import BaseTestClass

class ProductTestCase(BaseTestClass):

    service = ProductService()

    def test_get_by_id(self):
        product = self.service.get_product_by_id(3)

        for key in self.product_3.keys():
            self.assertEqual(self.product_3[key], getattr(product, key))

if __name__ == '__main__':
    unittest.main()
    