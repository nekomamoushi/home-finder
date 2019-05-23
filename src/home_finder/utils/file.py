# -*- coding: utf-8 -*-

from pathlib import Path
import yaml
import csv

from home_finder.utils.dropbox import dropbox_file_exists, dropbox_load_file


def yaml_load(filename, dropbox=None, storage="dropbox"):
    if storage == "local":
        file = Path(filename)
        if not file.exists():
            error_msg = "Local: <{0}> don't exists.".format(filename)
            raise Exception(error_msg)
        with file.open(mode='r') as fp:
            return yaml.safe_load(fp)
    elif storage == "dropbox":
        if not dropbox_file_exists(dropbox, filename):
            error_msg = "Dropbox: <{0}> don't exists.".format(filename)
            raise Exception(error_msg)
        data = dropbox_load_file(dropbox, filename)
        return yaml.safe_load(data)
    else:
        raise NotImplementedError()


def csv_load(filename, delimiter=';', storage="local"):
    if storage == "local":
        file = Path(filename)
        with file.open(mode='r') as fp:
            csv_reader = csv.reader(fp, delimiter=delimiter)
            data = [row for row in csv_reader]
        return data
    else:
        raise NotImplementedError()


def file_exists(filename):
    if Path(filename).expanduser().exists():
        return True
    return False


def build_filename(dirname, filename):
    return "{0}/{1}".format(dirname, filename)
