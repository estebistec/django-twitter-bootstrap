# -*- coding: utf-8 -*-


import datetime
import os

from django.core.cache import cache
import yaml


SITE_INFO_CACHE_KEY = u'site-info'


def site_info(request):
    return {
        u"site": _get_site_info()
    }


def _get_site_info():
    return cache.get(SITE_INFO_CACHE_KEY) or _load_site_info()


def _load_site_info():
    site_info_path = os.path.join(
        os.path.dirname(__file__),
        u'config',
        u'site_info.yml'
    )
    with open(site_info_path) as yaml_file:
        site_info = yaml.load(yaml_file)
        # Add extra info not in the file
        site_info.update(_get_extra_site_info())

        cache.set(SITE_INFO_CACHE_KEY, site_info)
        return site_info


def _get_extra_site_info():
    return {
        u"time": datetime.datetime.now()
    }
