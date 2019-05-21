# -*- coding: utf-8 -*-

from notifiers.ifttt import Ifttt

all_notifiers = {
    "ifttt": Ifttt
}

def notify(notifier_name, data, **kwargs):
    print(kwargs)
    print(all_notifiers.keys())
    if notifier_name in all_notifiers:
        notifier = all_notifiers[notifier_name](**kwargs)
        notifier.notify(data)
    else:
        raise Exception("<{0}> notifier does not exists.".format(notifier_name))
