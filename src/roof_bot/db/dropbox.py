# -*- coding: utf-8 -*-

import dropbox


def get_dropbox_object(token):
    dbx = dropbox.Dropbox(token)
    return dbx


def build_database(dbx, path, data):
    ids = "\n".join(data)
    ids_as_bytes = str.encode(ids)
    result = dbx.files_upload(ids_as_bytes, path)


def delete_database(dbx, path):
    result = dbx.files_delete(path)


def build_or_update_database_dropbox(token, path, data, update=False):
    dbx = get_dropbox_object(token)
    if update:
        delete_database(dbx, path)
    build_database(dbx, path, data)


def load_database_dropbox(token, path):
    dbx = get_dropbox_object(token)
    md, res = dbx.files_download(path)
    data_as_str = res.content.decode()
    return data_as_str.split('\n')

