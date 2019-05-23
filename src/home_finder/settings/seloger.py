# -*- coding: utf-8 -*-

from pathlib import Path

from utils.file import csv_load


INSEE_CODE_CITES_FILENAME = Path(__file__).parent.parent.parent.parent / "res" / "minified-code-postal-code-insee-iledefrance-2015.csv"


class SelogerSettings(object):

    SEARCH_URL = "https://www.seloger.com/list.htm"

    def __init__(self, settings):
        self._settings = settings

    @property
    def url(self):
        temp_url = self.SEARCH_URL
        temp_url += "?types=1&projects=2&enterprise=0&natures=1,2&picture=15"
        temp_url += "&surface={0}".format(self.process_surface())
        temp_url += "&rooms={0}".format(self.process_rooms())
        temp_url += "&bedrooms={0}".format(self.process_bedrooms())
        temp_url += "&price={0}".format(self.process_price())
        temp_url += "&places={0}".format(self.process_cities())
        temp_url += "&qsVersion=1.0"
        return temp_url

    def process_surface(self):
        s = self._settings.surface
        s_min = "NaN" if s[0] == 0 else s[0]
        s_max = "NaN" if s[1] == 0 else s[1]
        return "{0}/{1}".format(s_min, s_max)

    def process_rooms(self):
        return self._settings.rooms

    def process_bedrooms(self):
        return self._settings.bedrooms

    def process_price(self):
        p = self._settings.price
        p_min = "NaN" if p[0] == 0 else p[0]
        p_max = "NaN" if p[1] == 0 else p[1]
        return "{0}/{1}".format(p_min, p_max)

    def process_cities(self):
        def city_row(codes, city):
            for code in codes:
                if city == code[0]:
                    break
            else:
                error_msg = "ERROR: <{}> does not exists".format(city)
                error_msg += "ERROR: See {}".format(INSEE_CODE_CITES_FILENAME)
                raise Exception(error_msg)
            return code

        def process_code(code):
            if code == "75":
                return code
            return "{0}0{1}".format(code[0:2], code[2:])

        def build_places(places):
            # In:  [75, 940046]
            # Out: [{cp:75}|{ci:940046}]
            temp_places = ""
            for place in places:
                if place == "75":
                    temp_places += "{{cp:75}}|"
                else:
                    temp_places += "{{ci:{0}}}|".format(place)

            temp_places = temp_places.rstrip('|')
            return '[' + temp_places + ']'

        insee_codes = csv_load(INSEE_CODE_CITES_FILENAME)
        places = []
        for city in self._settings.cities:
            row = city_row(insee_codes, city.upper())
            processed = process_code(row[2])
            places.append(processed)

        return build_places(places)
