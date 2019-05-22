# -*- coding: utf-8 -*-

import requests
import logging

from notifiers.base import Notifier


class Ifttt(Notifier):

    NOTIFY_URL = "https://maker.ifttt.com/trigger/{0}/with/key/{1}"

    def __init__(self, credentials, trigger):
        self._credentials = credentials
        self._trigger = trigger
        self._logger = logging.getLogger(__name__)

    def process_data(self, data):
        payload = dict(
            value1=data["city"],
            value2=data["price"],
            value3=data["url"]
        )
        return payload

    def send(self, data):
        url = self.notification_url.format(self._trigger, self._credentials)
        r = requests.post(url, data=data)
        self.logger.debug("http status: <{0}>".format(r.status_code))
