from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from products_api.models.product import ProductModel


class ProductSchema(SQLAlchemyAutoSchema):
    """Schema class for marshalling input and output data for ProductModel."""

    class Meta:
        model = ProductModel
        include_relationships = True
        load_instance = True
