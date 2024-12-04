from marshmallow import validate, fields, Schema, post_load
from app.models.producto import Producto

class ProductoSchema(Schema):
    id_producto = fields.Integer(dump_only=True)
    nombre = fields.String(required=True)
    precio = fields.Float(required=True)
    activado = fields.Boolean(load_default=True)

    @post_load
    def make_producto(self, data, **kwargs):
        return Producto(**data)
    
