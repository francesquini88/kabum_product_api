from sqlalchemy import ARRAY, JSON, Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from products_api.models.database import Base

association_product_menu = Table(
    "association_product_menu",
    Base.metadata,
    Column("codigo_product", Integer, ForeignKey("products.codigo", ondelete="SET NULL")),
    Column("codigo_menu", Integer, ForeignKey("menus.codigo", ondelete="SET NULL")),
)


class ProductModel(Base):
    """Data Model class for storing Product ORM attributes and relationships."""

    __tablename__ = "products"

    # Primary key
    codigo = Column(Integer, primary_key=True, index=True)

    # Attributes
    brinde = Column(String, nullable=True)
    oferta_inicio = Column(Integer)
    vendedor_nome = Column(String, nullable=True)
    id_oferta = Column(String, nullable=True)
    nova_descricao = Column(String, nullable=True)
    menu = Column(String)
    nome = Column(String)
    fotos = Column(ARRAY(String))
    disponibilidade = Column(Boolean)
    pre_venda = Column(Boolean)
    preco = Column(Integer)
    preco_prime = Column(Integer)
    preco_desconto = Column(Integer)
    preco_desconto_prime = Column(Integer)
    preco_antigo = Column(Integer)
    economize_prime = Column(Integer)
    descricao = Column(String)
    tag_title = Column(String)
    tem_frete_gratis = Column(Boolean)
    frete_gratis_somente_prime = Column(Boolean)
    tag_description = Column(String)
    avaliacao_numero = Column(Integer)
    avaliacao_nota = Column(Integer)
    desconto = Column(Integer)
    is_openbox = Column(Boolean)
    produto_html = Column(String)
    dimensao_peso = Column(Integer)
    peso = Column(String)
    garantia = Column(String)
    codigo_anatel = Column(String)
    produto_especie = Column(Integer)
    link_descricao = Column(String)
    origem = Column(String, nullable=True)
    origem_nome = Column(String, nullable=True)
    flag_blackfriday = Column(Integer)
    sucesso = Column(Boolean)

    # Relationships
    menus = relationship("MenuModel", secondary=association_product_menu, lazy="joined")
    oferta = Column(JSON, nullable=True)
    familia = Column(JSON)
    fabricante = Column(JSON)
