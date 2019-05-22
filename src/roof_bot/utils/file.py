# -*- coding: utf-8 -*-

from pathlib import Path
import yaml
import csv


def yaml_load(filename, storage="local" ):
    if storage == "local":
        file = Path(filename)
        with file.open(mode='r') as fp:
            return yaml.safe_load(fp)
    else:
        raise NotImplementedError()

def csv_load(filename, delimiter=';', storage="local"):
    if storage == "local":
        file = Path(filename)
        with file.open(mode='r') as fp:
            csv_reader = csv.reader(fp, delimiter=delimiter)
            data = [ row for row in csv_reader]
        return data
    else:
        raise NotImplementedError()

def file_exists(filename):
    if Path(filename).expanduser().exists():
        return True
    return False

def build_filename(dirname, filename):
    return "{0}/{1}".format(dirname, filename)
