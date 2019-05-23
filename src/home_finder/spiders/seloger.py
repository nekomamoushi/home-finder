# -*- coding: utf-8 -*-

from math import ceil

from lxml import html
from parse import parse

from spiders.base import Spiderman


class SeLogerSpider(Spiderman):

    NAME = "seloger"
    CSS_SELECTOR_FOR_ADS_NUMBER = 'div.title_nbresult'
    CSS_SELECTOR_FOR_RESULTS_LIST = 'section.liste_resultat'
    CSS_SELECTOR_LIST_FOR_ADS = [
        'div.c-pa-list.c-pa-sl.cartouche',
        'div.c-pa-list.c-pa-sl9.cartouche',
        'div.c-pa-list.c-pa-bd.cartouche',
    ]

    def start_urls(self):

        def make_url(base, var, page_number):
            return base + var + str(page_number)

        listing_var = "&LISTING-LISTpg="
        nb_ads, nb_pages = self.ads_number()
        self.logger.info("Found {} results.".format(nb_ads))
        nb_pages = int(nb_pages)
        urls = [
            make_url(self._search_url, listing_var, n)
            for n in range(1, nb_pages + 1)
        ]
        return urls

    def ads_number(self):
        content = self.make_request(self._search_url)

        root = html.fromstring(content)
        # Parse HTML and get total announces string
        results = root.cssselect(self.CSS_SELECTOR_FOR_ADS_NUMBER)
        results = results[0].text_content().strip()
        # Parse String and total number
        nb_results = parse("{} annonces", results)[0]
        nb_pages = ceil(int(nb_results) / 20)
        return (int(nb_results), nb_pages)

    def process_page(self, content):
        root = html.fromstring(content)

        # Parse HTML and get results list
        results = root.cssselect(self.CSS_SELECTOR_FOR_RESULTS_LIST)
        # results is a list of one element so return the first one
        results = results[0]

        ads = []
        for selector in self.CSS_SELECTOR_LIST_FOR_ADS:
            selector_results = results.cssselect(selector)
            ads.extend(selector_results)
        return ads

    def process_element(self, element):
        ad_url = element[1][0].get('href')
        size = element[1][1][2].text_content()
        price = element[1][2][1].text_content().strip()
        city = element[1][4].text_content().strip()
        ad_id = element[1][5].get('data-idannonce')
        ad_publication_id = element[1][5].get('data-idpublication')
        return {
            'id': ad_id,
            'pub_id': ad_publication_id,
            'url': ad_url,
            'city': city,
            'size': size,
            'price': price
        }
