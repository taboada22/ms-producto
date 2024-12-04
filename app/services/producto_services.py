from app.models.producto import Producto
from app.repositories.producto_repository import ProductoRepository
from app import cache

class ProductoService:
    def __init__(self):
        self.repository = ProductoRepository()

    def add_producto(self, producto:Producto) -> Producto:
        return self.repository.save(producto)

    def delete_producto(self, producto_id: int) -> None:
        producto = self.repository.find_by_id(producto_id)
        if producto:
            self.repository.delete(producto)

    def get_producto(self, producto_id: int) -> Producto:
        result = None
        if producto_id is not None:
            result = cache.get(f"producto_{id}")
            if result is None:
                result = self.repository.find_by_id(producto_id)
                cache.set(f"producto_{id}", result, 50)
        return result    

    def get_producto_by_nombre(self, nombre: str) -> Producto:
        return self.repository.find_by_nombre(nombre)

