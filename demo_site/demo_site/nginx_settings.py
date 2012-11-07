# -*- coding: utf-8 -*-


from .settings import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATIC_URL = "http://localhost:8080/static/"
