# -*- coding: utf-8 -*-

from utils.file import yaml_load


class Settings(object):

    def __init__(self, filename):
        self._filename = filename
        self.load()

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

    @property
    def notifier_name(self):
        return self._settings["notification"]["name"]

    @property
    def notifier_type(self):
        return self._settings["notification"]["required"]["type"]

    @property
    def notifier_trigger(self):
        return self._settings["notification"]["required"]["trigger"]

    @property
    def notifier_token(self):
        return self._notifier_token

    @notifier_token.setter
    def notifier_token(self, token):
        self._notifier_token = token

    @property
    def dropbox_token(self):
        self._dropbox_token

    @dropbox_token.setter
    def dropbox_token(self, token):
        self._dropbox_token = token
