from contextlib import contextmanager
from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from products_api.environment import DB

Base = declarative_base()

_SQLALCHEMY_DATABASE_URL = f"postgresql://{DB.user}:{DB.password}@{DB.host}:{DB.port}/{DB.name}"

engine = create_engine(_SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Verify if all tables exist. If they do not, create them
def verify_and_create_db_tables() -> None:
    """Create all database tables based on defined models metadata if they are not created yet."""
    Base.metadata.create_all(bind=engine)


@contextmanager
def get_db() -> Iterator[Session]:
    """Yield a database session to perform operations and close after it is done."""
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()
