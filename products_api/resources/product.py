from typing import List

from flask_restful import Resource

from products_api.models.database import get_db
from products_api.models.product import ProductModel
from products_api.schemas.product import ProductSchema


class ProductList(Resource):
    """Controller class that provides a HTTP GET endpoint for all ProductModel objects."""

    def get(self) -> List[ProductSchema]:
        with get_db() as db_session:
            products = db_session.query(ProductModel).all()
            return ProductSchema().dump(products, many=True)


class Product(Resource):
    """Controller class that provides a HTTP GET endpoint for a single ProductModel object."""

    def get(self, product_id: str) -> ProductSchema:
        with get_db() as db_session:
            product = (
                db_session.query(ProductModel).filter(ProductModel.codigo == product_id).first()
            )
            return ProductSchema().dump(product, many=False)

    def delete(self, product_id: str) -> None:
        with get_db() as db_session:
            product = (
                db_session.query(ProductModel).filter(ProductModel.codigo == product_id).first()
            )
            db_session.delete(product)
            db_session.commit()
