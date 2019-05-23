# -*- coding: utf-8 -*-

from pathlib import Path
import logging

from db.local import build_or_update_database_local, load_database_local

logger = logging.getLogger(__name__)


DROPBOX_DATABASE_DIRECTORY = Path("/home-finder")


def get_database_file(provider, storage="dropbox"):
    if storage == "dropbox":
        return DROPBOX_DATABASE_DIRECTORY / provider
    else:
        raise NotImplementedError("You can only use dropbox storage")


def build_or_update_database(storage, path, data, update=False):
    if storage == "local":
        build_or_update_database_local(path, data, update)
    else:
        raise NotImplementedError("You can only usr local storage")


def load_database(storage, path):
    if storage == "local":
        return load_database_local(path)
    else:
        raise NotImplementedError("You can only usr local storage")
