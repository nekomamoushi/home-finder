# -*- coding: utf-8 -*-

from pathlib import Path
import logging

from settings.settings import Settings
from utils.file import build_filename, file_exists
from utils.misc import filter_ids, compare_ids
from db.common import build_or_update_database, load_database
from providers import get_provider, all_providers

logger = logging.getLogger(__name__)

SETTINGS_FILENAME = Path("~").expanduser() / ".local" / "roof-bot" / "settings.yml"
DATABASE_DIRECTORY = Path("~").expanduser() / ".local" / "roof-bot"

def check_settings():
    if not file_exists(SETTINGS_FILENAME):
        error_msg = "<{0}> don't exists.".format(filename)
        raise Exception(error_msg)
    return Settings(SETTINGS_FILENAME)

def verify_new_ads(storage, database, new_results):
    old_ids = load_database(storage, database)
    new_ids = filter_ids(new_results)
    diff_ids = compare_ids(old_ids, new_ids)

    new_ads = []
    for ad in new_results:
        for diff_id in diff_ids:
            if diff_id == ad['id']:
                new_ads.append(ad)

    if not new_ads:
        logger.info("There is no new ads")
    else:
        logger.info("There is {0} new ads".format(len(new_ads)))

def execute(settings):
    for provider_name in all_providers:
        # Get provider
        provider = get_provider(provider_name)
        # Get Preferences
        preferences = provider.preferences(settings)
        # Get Spider
        spider = provider.spider(preferences.url, delay=1)
        # Get results
        results = spider.crawl()

        # Create database if not exists
        db_file = build_filename(DATABASE_DIRECTORY, provider_name)
        if file_exists(db_file):
            verify_new_ads("local", db_file, results)
            build_or_update_database("local", db_file, results, update=True)
            spider.close()
            exit(0)

        build_or_update_database("local", db_file, results)
        spider.close()


