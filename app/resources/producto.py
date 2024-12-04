from flask import Blueprint, request, jsonify
from app.services.producto_services import ProductoService
from app.schema.producto_schema import ProductoSchema

producto = Blueprint('producto', __name__, url_prefix='/api/producto')
service = ProductoService()
producto_schema = ProductoSchema()

@producto.route('/agregarproducto', methods=['POST'])
def add_product():
    producto_data = service.add_producto(producto_schema.load(request.json))
    return producto_schema.dump(producto_data), 200

@producto.route('/delete/<int:id>', methods=['DELETE'])  
def delete_product(id):
    service.delete_producto(id)
    return '', 200

@producto.route('/find_by_id/<int:id>',methods=['GET'])
def get_product(id):
    producto = producto_schema.dump(service.get_producto(id))
    if producto is None:
        return jsonify({'message': 'Not found'}), 404
    return producto

@producto.route('/find_by_nombre/<string:nombre>',methods=['GET'])
def get_producto_by_nombre():
    producto = producto_schema.load(request.json)
    return producto_schema.dump(service.get_producto_by_nombre(producto['nombre']))
