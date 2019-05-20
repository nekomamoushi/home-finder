# -*- coding: utf-8 -*-

from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def build_or_update_database_local(path, data, update=False):
    if udpdate:
        delete_database(path)
    build_database(path, data)

def delete_database(path):
    logger.debug("Deleting {0}".format(path))
    Path(path).unlink()

def build_database(path, data):
    db = Path(path)
    with db.open(mode='w') as fp:
            fp.write(data)
