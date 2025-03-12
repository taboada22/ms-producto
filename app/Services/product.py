from app import cache
from app.Models.product import Product
from app.Repositories.product import ProductRepository
from app.Services.format_logs import format_logs
from dataclasses import dataclass

logging = format_logs('ProductServices')

@dataclass
class ProductService:  
    
    repository = ProductRepository()  

    def get_product_by_id(self, id_product: int) -> Product:
        product = cache.get(f'product_{id_product}')
        if product is None:
            product = self.repository.find_by_id(id_product)
            cache.set(f'product_{id_product}', product, timeout=60)
            logging.info(f'product_{product.id_product} added to cache')

        logging.info(f'product_{product.id_product} retrieved to cache')    
        return product
