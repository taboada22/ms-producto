from flask import Blueprint, render_template, request
from app.Services.product import ProductService
from app.Schema.product import product_schema, products_schema

product = Blueprint('product', __name__, url_prefix='/api/products')
services = ProductService()

@product.route('/get_by_id/<int:id>',methods=['GET'])
def get_by_id(id):
    try:
        status_code = 200
        return product_schema.dumps(services.get_product_by_id(id)), status_code
    except:
        status_code = 404
        return product_schema.dumps(services.get_product_by_id(id)), status_code
