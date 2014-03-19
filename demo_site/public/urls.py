# -*- coding: utf-8 -*-


from django.conf.urls import patterns
from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from . import views


urlpatterns = patterns('',
    (r'^index/$', RedirectView.as_view(url=reverse_lazy(u"home"))),
    url(r'^$', views.home, name=u"home"),
    url(r'^components/$', views.components, name=u"components"),
    url(r'^css/$', views.css, name=u"css"),
    url(r'^customize/$', views.customize, name=u"customize"),
    url(r'^getting-started/$', views.getting_started, name=u"getting-started"),
    url(r'^javascript/$', views.javascript, name=u"javascript"),
    url(r'^about/$', views.about, name=u"about"),
    url(r'^migration/$', views.migration, name=u"migration"),
)
