# -*- coding: utf-8 -*-

from settings.seloger import SelogerSettings
from spiders.seloger import SeLogerSpider


class Provider(object):

    def __init__(self, preferences_class, spider_class):
        self._preferences_class = preferences_class
        self._spider_class = spider_class

    @property
    def preferences(self):
        return self._preferences_class

    @property
    def spider(self):
        return self._spider_class

all_providers = {
    "seloger": Provider(SelogerSettings, SeLogerSpider)
}

def get_provider(provider_name):
    if provider_name in all_providers:
        provider = all_providers[provider_name]
        return provider
    else:
        raise Exception("<{0}> provider does not exists.".format(provider_name))
