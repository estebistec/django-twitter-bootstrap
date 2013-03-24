# -*- coding: utf-8 -*-


from .settings import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
STATIC_URL = "http://localhost:8080/static/"
