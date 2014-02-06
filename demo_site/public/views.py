# -*- coding: utf-8 -*-


from django.views.generic import TemplateView


class PageView(TemplateView):
    page_slug = None
    page_title = None
    page_lead = None
    page_nav = None

    def get_page_data(self):
        return {
            u"slug": self.page_slug,
            u"title": self.page_title,
            u"lead": self.page_lead,
            u"nav": self.page_nav,
            u"base_url": u"/"
        }

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        context[u'page'] = self.get_page_data()
        return context


class HomePageView(PageView):
    template_name = u"index.html"
    page_slug = u"home"
    page_title = u"Bootstrap"


class ComponentsPageView(PageView):
    template_name = u"components.html"
    page_slug = u"components"
    page_title = u"Components"
    page_lead = u"Over a dozen reusable components built to provide iconography, dropdowns, input groups, navigation, alerts, and much more."
    page_nav = u'_includes/nav-components.html'


class CSSPageView(PageView):
    template_name = u"css.html"
    page_slug = u"css"
    page_title = u"CSS"
    page_lead = u"Global CSS settings, fundamental HTML elements styled and enhanced with extensible classes, and an advanced grid system."
    page_nav = u'_includes/nav-css.html'


class CustomizePageView(PageView):
    template_name = u"customize.html"
    page_slug = u"customize"
    page_title = u"Customize and download"
    page_lead = u"Customize Bootstrap's components, Less variables, and jQuery plugins to get your very own version."
    page_nav = u'_includes/nav-customize.html'


class GettingStartedPageView(PageView):
    template_name = u"getting-started.html"
    page_slug = u"getting-started"
    page_title = u"Getting started"
    page_lead = u"An overview of Bootstrap, how to download and use, basic templates and examples, and more."
    page_nav = u'_includes/nav-getting-started.html'


class JavaScriptPageView(PageView):
    template_name = u"javascript.html"
    page_slug = u"js"
    page_title = u"JavaScript"
    page_lead = u"Bring Bootstrap's components to life with over a dozen custom jQuery plugins. Easily include them all, or one by one."
    page_nav = u'_includes/nav-javascript.html'


class AboutPageView(PageView):
    template_name = u"about.html"
    page_slug = u"about"
    page_title = u"About"
    page_lead = u"Learn about the project's history, meet the maintaining teams, and find out how to use the Bootstrap brand."
    page_nav = u'_includes/nav-about.html'


class MigrationPageView(PageView):
    template_name = u"migration.html"
    page_slug = u"migration"
    page_title = u"Migrating to v3.x"
    page_lead = u"Guidance on how to upgrade from Bootstrap v2.x to v3.x with emphasis on major changes, what's new, and what's been removed."
    page_nav = u"_includes/nav-migration.html"


home = HomePageView.as_view()
components = ComponentsPageView.as_view()
css = CSSPageView.as_view()
customize = CustomizePageView.as_view()
getting_started = GettingStartedPageView.as_view()
javascript = JavaScriptPageView.as_view()
about = AboutPageView.as_view()
migration = MigrationPageView.as_view()
