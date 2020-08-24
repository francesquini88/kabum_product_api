from typing import List

from flask_restful import Resource

from products_api.models.database import get_db
from products_api.models.menu import MenuModel
from products_api.schemas.menu import MenuSchema


class MenuList(Resource):
    """Controller class that provides a HTTP GET endpoint for all MenuModel objects."""

    def get(self) -> List[MenuSchema]:
        with get_db() as db_session:
            menus = db_session.query(MenuModel).all()
            return MenuSchema().dump(menus, many=True)


class Menu(Resource):
    """Controller class that provides a HTTP GET endpoint for a single MenuModel object."""

    def get(self, menu_id: str) -> MenuSchema:
        with get_db() as db_session:
            menu = db_session.query(MenuModel).filter(MenuModel.codigo == menu_id).first()
            return MenuSchema().dump(menu, many=False)

    def delete(self, menu_id: str) -> None:
        with get_db() as db_session:
            menu = db_session.query(MenuModel).filter(MenuModel.codigo == menu_id).first()
            db_session.delete(menu)
            db_session.commit()
