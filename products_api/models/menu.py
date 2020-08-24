from sqlalchemy import Column, Integer, String

from products_api.models.database import Base


class MenuModel(Base):
    """Data Model class for storing Menu ORM attributes and relationships."""

    __tablename__ = "menus"

    # Primary key
    codigo = Column(Integer, primary_key=True, index=True)

    # Attributes
    nome = Column(String)
    amigavel = Column(String)
    nome_url = Column(String)
