# -*- coding: utf-8 -*-

from pathlib import Path
import logging

from home_finder.db.dropbox import build_or_update_database_dropbox, load_database_dropbox
from home_finder.db.local import build_or_update_database_local, load_database_local
from home_finder.utils.misc import filter_ids


logger = logging.getLogger(__name__)
DROPBOX_DATABASE_DIRECTORY = Path("/home-finder")


def get_database_file(provider, storage="dropbox"):
    if storage == "dropbox":
        full_path = DROPBOX_DATABASE_DIRECTORY / provider
        return str(full_path)
    else:
        raise NotImplementedError("You can only use dropbox storage")


def build_or_update_database(dbx, path, data, update=False, storage="dropbox"):
    data = filter_ids(data)
    if storage == "dropbox":
        build_or_update_database_dropbox(dbx, path, data, update)
    else:
        raise NotImplementedError("You can only use dropbox storage")


def load_database(dbx, path, storage="dropbox"):
    if storage == "dropbox":
        return load_database_dropbox(dbx, path)
    else:
        raise NotImplementedError("You can only use dropbox storage")
