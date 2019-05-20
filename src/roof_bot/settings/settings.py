# -*- coding: utf-8 -*-

import yaml

from utils.file import yaml_load


class Settings(object):

    def __init__(self, filename):
        self._filename = filename

    def load(self):
        self._settings = yaml_load(self._filename)

    def display(self):
        print(self._settings)

    @property
    def surface(self):
        s = self._settings["search"]["surface"]
        return (s["min"], s["max"])

    @property
    def price(self):
        p = self._settings["search"]["price"]
        return (p["min"], p["max"])

    @property
    def rooms(self):
        return self._settings["search"]["rooms"]

    @property
    def bedrooms(self):
        return self._settings["search"]["bedrooms"]

    @property
    def cities(self):
        return self._settings["search"]["cities"]

