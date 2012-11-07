# -*- coding: utf-8 -*-


from django.conf.urls import patterns
from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView


urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': reverse_lazy('index')}),
    url(r'^base-css\.html$', TemplateView.as_view(template_name='base-css.html'), name='base-css'),
    url(r'^components\.html$', TemplateView.as_view(template_name='components.html'), name='components'),
    url(r'^customize\.html$', TemplateView.as_view(template_name='customize.html'), name='customize'),
    url(r'^extend\.html$', TemplateView.as_view(template_name='extend.html'), name='extend'),
    url(r'^getting-started\.html$', TemplateView.as_view(template_name='getting-started.html'), name='getting-started'),
    url(r'^index\.html$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^javascript\.html$', TemplateView.as_view(template_name='javascript.html'), name='javascript'),
    url(r'^scaffolding\.html$', TemplateView.as_view(template_name='scaffolding.html'), name='scaffolding'),
    url(r'^examples/carousel\.html$', TemplateView.as_view(template_name='examples/carousel.html'), name='examples-carousel'),
    url(r'^examples/fluid\.html$', TemplateView.as_view(template_name='examples/fluid.html'), name='examples-fluid'),
    url(r'^examples/hero\.html$', TemplateView.as_view(template_name='examples/hero.html'), name='examples-hero'),
    url(r'^examples/marketing-alternative\.html$', TemplateView.as_view(template_name='examples/marketing-alternative.html'), name='examples-marketing-alternative'),
    url(r'^examples/marketing-narrow\.html$', TemplateView.as_view(template_name='examples/marketing-narrow.html'), name='examples-marketing-narrow'),
    url(r'^examples/signin\.html$', TemplateView.as_view(template_name='examples/signin.html'), name='examples-signin'),
    url(r'^examples/starter-template\.html$', TemplateView.as_view(template_name='examples/starter-template.html'), name='examples-starter-template'),
    url(r'^examples/sticky-footer\.html$', TemplateView.as_view(template_name='examples/sticky-footer.html'), name='examples-sticky-footer'),
)
