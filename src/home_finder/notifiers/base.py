# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import logging


class Notifier(metaclass=ABCMeta):

    NOTIFY_URL = None

    def __init__(self):
        self._logger = logging.getLogger(__name__)

    @property
    def logger(self):
        return self._logger

    @property
    def notification_url(self):
        return self.NOTIFY_URL

    @abstractmethod
    def process_data(self, data):
        pass

    @abstractmethod
    def send(self, data):
        pass

    def notify(self, data):
        data = self.process_data(data)
        self.send(data)
