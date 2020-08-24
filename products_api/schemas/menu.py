from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from products_api.models.menu import MenuModel


class MenuSchema(SQLAlchemyAutoSchema):
    """Schema class for marshalling input and output data for MenuModel."""

    class Meta:
        model = MenuModel
        include_relationships = True
        load_instance = True
