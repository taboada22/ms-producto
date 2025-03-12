from app import db
from sqlalchemy.exc import IntegrityError, NoResultFound
from app.Models.product import Product
from app.Services.format_logs import format_logs

logging = format_logs('ProductRepository')

class ProductRepository:

    def find_by_id(self, id: int) -> Product :
        try:
            res = db.session.query(Product).filter(Product.id_product == id).one()
            logging.info(f'Product with id {id} found successfully')
            return res
        except NoResultFound as e:
            logging.error(f'Product id {id} not found, error {e}')
            return e