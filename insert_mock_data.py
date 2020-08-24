import glob
import json

from products_api.models import MenuModel, ProductModel
from products_api.models.database import get_db, verify_and_create_db_tables

verify_and_create_db_tables()

print("Populating local database with mock data...")

with get_db() as db_session:
    for filepath in glob.glob("db_mock_products/*.json"):
        with open(filepath, "r") as file:
            product_data = json.load(file)

            menu_array = []
            for menu_data in product_data["menus"]:
                menu_id = menu_data["codigo"]
                if db_session.query(MenuModel).filter(MenuModel.codigo == menu_id).first():
                    continue

                menu_model = MenuModel(**menu_data)
                db_session.add(menu_model)
                menu_array.append(menu_model)

            product_data["menus"] = menu_array
            product = ProductModel(**product_data)
            db_session.add(product)

        db_session.commit()

print("Done!")
