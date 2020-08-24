import logging

from products_api.app import create_app
from products_api.environment import Server
from products_api.models.database import verify_and_create_db_tables


def logging_setup() -> None:
    """Setup logging configuration for working with gunicorn WSGI HTTP Server."""
    log_fmt = "%(asctime)s | %(levelname)-8s | %(message)s   (%(filename)s:%(funcName)s)"
    date_fmt = "%d/%m/%Y %H:%M:%S"

    log_levels_dict = {"DEBUG": 10, "INFO": 20, "WARNING": 30, "ERROR": 40}
    log_level = log_levels_dict[Server.logging_level]

    # Create file and console logging handlers for the root logging
    logging.basicConfig(format=log_fmt, datefmt=date_fmt, level=log_level)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(logging.Formatter(fmt=log_fmt, datefmt=date_fmt))

    loggers = [
        logging.getLogger("gunicorn"),
        logging.getLogger("gunicorn.access"),
        logging.getLogger("gunicorn.error"),
        logging.getLogger("uvicorn"),
        logging.getLogger("uvicorn.access"),
        logging.getLogger("uvicorn.error"),
    ]

    for logger in loggers:
        logger.handlers = [console_handler]


logging_setup()

verify_and_create_db_tables()

app = create_app()
