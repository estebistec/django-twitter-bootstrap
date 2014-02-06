# -*- coding: utf-8 -*-


import datetime
import os

from django.core.cache import cache
import yaml


SITE_INFO_CACHE_KEY = u'site-info'
PUBLIC_APP_PATH = os.path.dirname(__file__)


def site_info(request):
    return {
        u"site": _get_site_info()
    }


def _get_site_info():
    site_info =  cache.get(SITE_INFO_CACHE_KEY) or _load_site_info()
    # Add extra info not in the files
    site_info.update(_get_extra_site_info())
    return site_info


def _load_site_info():
    site_info_path = os.path.join(PUBLIC_APP_PATH, u'_config.yml')
    site_info = _load_yaml_file(site_info_path)
    site_info['data'] = _load_data_files()
    cache.set(SITE_INFO_CACHE_KEY, site_info)
    return site_info


def _load_data_files():
    data = {}
    data_dir = os.path.join(PUBLIC_APP_PATH, u'_data')
    for filename in os.listdir(data_dir):
        name, ext = os.path.splitext(filename)
        if ext == '.yml':
            data[name] = _load_yaml_file(os.path.join(data_dir, filename))
    return data


def _load_yaml_file(yaml_path):
    with open(yaml_path) as yaml_file:
        return yaml.load(yaml_file)


def _get_extra_site_info():
    return {
        u"time": datetime.datetime.now()
    }
