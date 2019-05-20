# -*- coding: utf-8 -*-

import logging
from local import build_or_update_database_local

logger = logging.getLogger(__name__)

def build_or_update_database(storage, path, data, update=False):
    if storage == "local":
        build_or_update_database_local(path, data, update)
    else:
        raise NotImplementedError("You can only usr local storage")
