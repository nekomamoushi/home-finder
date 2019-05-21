# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import random
from time import sleep
import logging
import warnings

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from utils.http import get_user_agent

class Spiderman(metaclass=ABCMeta):

    NAME = None

    def __init__(self, search_url, delay=3):
        self._search_url = search_url
        self._delay = delay
        if delay <= 1:
            warnings.warn("Becareful delay={0}, be gentle when scraping".format(delay))
        self._logger = logging.getLogger(__name__)
        self.start()

    @property
    def logger(self):
        return self._logger

    # Open headless chromedriver
    def start(self):
        self.logger.debug("Starting webdriver")

        # Firefox options
        options = Options()
        options.headless = True

        # Firefox profile
        profile = webdriver.FirefoxProfile()
        user_agent = get_user_agent()
        profile.set_preference("general.useragent.override", user_agent)
        # 1 - Allow all images
        # 2 - Block all images
        # 3 - Block 3rd party images
        profile.set_preference("permissions.default.image", 2)

        # Firefox session
        self.driver = webdriver.Firefox(options=options, firefox_profile=profile)
        self.driver.implicitly_wait(15)

	# Close chromedriver
    def close(self):
        self.logger.debug("Closing webdriver")
        self.driver.quit()

    # Tell the browser to get a page
    def make_request(self, url):
        self.driver.get(url)
        sleep(self._delay)
        return self.driver.page_source

    @property
    def url_base(self):
        return self._url_base

    @abstractmethod
    def start_urls(self):
        pass

    @abstractmethod
    def crawl(self):
        pass

    def process(self, urls):
        results = []
        for url in urls:
            content = self.make_request(url)
            ads = self.process_page(content)
            for ad in ads:
                results.append(self.process_element(ad))
        return results

    @abstractmethod
    def process_page(self, url):
        pass

    @abstractmethod
    def process_element(self, element):
        pass

