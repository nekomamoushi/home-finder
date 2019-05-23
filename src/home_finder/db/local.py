# -*- coding: utf-8 -*-

from pathlib import Path
import logging

from home_finder.utils.misc import filter_ids

logger = logging.getLogger(__name__)


def build_or_update_database_local(path, data, update=False):
    if update:
        delete_database(path)
    build_database(path, data)


def load_database_local(path):
    with open(path, 'r') as reader:
        ids = [line.strip('\n') for line in reader.readlines()]
    return ids


def delete_database(path):
    logger.debug("Deleting {0}".format(path))
    Path(path).unlink()


def build_database(path, data):
    logger.debug("Building {0}".format(path))
    db = Path(path)
    with db.open(mode='w') as fp:
        ids = filter_ids(data)
        for ad_id in ids:
            fp.write(ad_id + '\n')
