
import logging
from logging.config import dictConfig
import logging.handlers

import sys

STANDARD_FORMAT = "%(asctime)s - %(name)s - %(levelname)s : %(message)s"
SHORT_FORMAT = "%(name)s : %(message)s"

DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
}

def setup_logging(log_level=logging.INFO):
    dictConfig(DEFAULT_LOGGING)

    stream_handler = get_stream_handler(sys.stdout, logging.DEBUG, SHORT_FORMAT)
    logging.root.addHandler(stream_handler)

    rotate_file_handler = get_rotate_file_handler('/tmp/roof-bot.log', logging.DEBUG, STANDARD_FORMAT)
    logging.root.addHandler(rotate_file_handler)

    logging.root.setLevel(log_level)

def setup_logging_dependencies(log_level=logging.WARNING):
    logging.getLogger("selenium").setLevel(level)
    logging.getLogger("urllib3").setLevel(level)
    logging.getLogger("parse").setLevel(level)

#-----------------------------------------------------------------------------#

def get_stream_handler(stream, level, format_):
    handler = logging.StreamHandler(stream)

    formatter = logging.Formatter(format_)
    handler.setFormatter(formatter)

    handler.setLevel(level)

    return handler

def get_rotate_file_handler(filename, level, format_):
    handler = logging.handlers.RotatingFileHandler(
        filename,
        maxBytes=100000,
        backupCount=1,
        encoding="utf8"
    )

    formatter = logging.Formatter(format_)
    handler.setFormatter(formatter)

    handler.setLevel(level)

    return handler
