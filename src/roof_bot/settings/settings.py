# -*- coding: utf-8 -*-

from utils.dropbox import get_dropbox_object
from utils.file import yaml_load


class Settings(object):

    def __init__(self, filename, dropbox_token, notifier_token):
        self._filename = filename
        self._dropbox = get_dropbox_object(dropbox_token)
        self._notifier_token = notifier_token
        self.load()

    def load(self):
        self._settings = yaml_load(self._filename, self._dropbox)

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

    @property
    def dropbox(self):
        self._dropbox

