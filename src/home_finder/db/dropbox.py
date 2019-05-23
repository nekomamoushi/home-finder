# -*- coding: utf-8 -*-

from utils.dropbox import get_dropbox_object
from utils.dropbox import dropbox_load_file
from utils.dropbox import dropbox_create_file, dropbox_delete_file


def build_database(dbx, path, data):
    dropbox_create_file(dbx, path, data)


def delete_database(dbx, path):
    dropbox_delete_file(dbx, path)


def build_or_update_database_dropbox(dbx, path, data, update=False):
    if update:
        delete_database(dbx, path)
    build_database(dbx, path, data)


def load_database_dropbox(dbx, path):
    data = dropbox_load_file(dbx, path)
    return data.split('\n')

