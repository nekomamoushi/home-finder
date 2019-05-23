# -*- coding: utf-8 -*-

from home_finder.notifiers.ifttt import Ifttt

all_notifiers = {
    "ifttt": Ifttt
}


def notify(notifier_name, data, **kwargs):
    if notifier_name in all_notifiers:
        notifier = all_notifiers[notifier_name](**kwargs)
        notifier.notify(data)
    else:
        raise Exception("<{0}> notifier doesn't exists.".format(notifier_name))
