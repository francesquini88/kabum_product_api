import os


class Server:
    """Create API Server environment variables."""

    logging_level: str = os.environ["LOGGING_LEVEL"]


class DB:
    """Create PostgreSQL environment variables."""

    name: str = os.environ["DATABASE_NAME"]
    user: str = os.environ["DATABASE_USERNAME"]
    password: str = os.environ["DATABASE_PASSWORD"]
    host: str = os.environ["DATABASE_HOST"]
    port: str = os.environ["DATABASE_PORT"]
