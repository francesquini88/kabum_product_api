from flask import Flask
from flask_restful import Api

from products_api.resources import menu, product


def create_app() -> Flask:
    """Create, setup and return an instance of Flask app."""
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(product.ProductList, "/products")
    api.add_resource(product.Product, "/products/<product_id>")

    api.add_resource(menu.MenuList, "/menus")
    api.add_resource(menu.Menu, "/menus/<menu_id>")

    return app
