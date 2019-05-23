# -*- coding: utf-8 -*-


def filter_ids(results):
    ids = [result['id'] for result in results]
    return ids


def compare_ids(old_ids, new_ids):
    diff_ids = []
    for _id in new_ids:
        if _id not in old_ids:
            diff_ids.append(_id)
    return diff_ids
