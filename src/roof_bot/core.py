# -*- coding: utf-8 -*-

import os
from pathlib import Path
import logging

from settings.settings import Settings
from utils.dropbox import dropbox_file_exists
from utils.misc import filter_ids, compare_ids
from db.common import get_database_file, build_or_update_database, load_database
from providers import get_provider, all_providers
from notifiers import notify

logger = logging.getLogger(__name__)

HOME = Path("~").expanduser()
SETTINGS_FILENAME = "/home-finder/settings.yml"
DATABASE_DIRECTORY = HOME / ".local" / "roof-bot"


def check_settings():
    dropbox_token = check_dropbox_token()
    notifier_token = check_notifier_token()
    settings = Settings(SETTINGS_FILENAME, dropbox_token, notifier_token)
    return settings


def check_notifier_token():
    notifier_token = os.environ.get("NOTIFIER_TOKEN", None)
    if not notifier_token:
        raise Exception("You need to set NOTIFIER_TOKEN")
    return notifier_token


def check_dropbox_token():
    dropbox_token = os.environ.get("DROPBOX_TOKEN", None)
    if not dropbox_token:
        raise Exception("You need to set DROPBOX_TOKEN")
    return dropbox_token


def verify_new_ads(dbx, database, new_results):
    old_ids = load_database(dbx, database)
    new_ids = filter_ids(new_results)
    diff_ids = compare_ids(old_ids, new_ids)

    new_ads = []
    for ad in new_results:
        for diff_id in diff_ids:
            if diff_id == ad['id']:
                new_ads.append(ad)

    if not new_ads:
        logger.info("There is no new ads")
        return None

    logger.info("There is {0} new ads".format(len(new_ads)))
    return new_ads


def notify_new_ads(new_ads, settings):
    notifier = settings.notifier_name
    token = settings.notifier_token
    trigger = settings.notifier_trigger

    for ad in new_ads:
        notify(notifier, ad, credentials=token, trigger=trigger)


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
        database_path = get_database_file(provider_name)
        if dropbox_file_exists(settings.dropbox, database_path):
            new_ads = verify_new_ads(settings.dropbox, database_path, results)
            if new_ads:
                notify_new_ads(new_ads, settings)
            build_or_update_database(settings.dropbox, database_path, results, update=True)
            spider.close()
            exit(0)

        build_or_update_database(settings.dropbox, database_path, results)
        spider.close()
