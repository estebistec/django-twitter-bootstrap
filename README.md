## Overview

This package provides a [Django](https://www.djangoproject.com) app whose
static folder contains the sources of
[Twitter Bootstrap](http://twitter.github.com/bootstrap), nothing more and
nothing less. The un-minified [LESS](http://lesscss.org) and JavaScript sources
are included to be integrated into your Django site as you see fit. If you
simply want to use the minified CSS and JS files provided by the Bootstrap
project, you probably don't need this anyway.

Further goals of this project include:

 * To include Bootstrap as a git submodule, so as to include specific release
   tags and avoid the mess of managing a copy of Bootstrap.
 * To provide versions that mirror Bootstrap releases going forward.
 * To provide a simple example project that demonstrates usage.

And that's it! Twitter Bootstrap pre-packaged for Django.

I found that other similar projects:

 * Did not keep up with recent versions of Bootstrap.
 * Simply made a copy of the Bootstrap sources, messy and unecessary.
 * Tied the packaging to their own clever template tags or other Django
   components. You should have your choice of these things apart from this
   packaging.

## Setup

A sample working project can be found
[here](https://github.com/estebistec/django-twitter-bootstrap/tree/master/demo_site).

First, install the app:

```bash
pip install django-twitter-bootstrap
```

Then include it in your Django project.

```python
# settings.py:

INSTALLED_APPS = (
    ...
    'twitter_bootstrap',
    ...
)
```

This also assumes you haven't removed
`django.contrib.staticfiles.finders.AppDirectoriesFinder` from the
`STATICFILES_FINDERS` config setting.

## Provided staticfiles

Of course what's provided is just Bootstrap, but more specifically...

### LESS

 * `less/bootstrap.less`
 * `less/responsive.less`

Also included are lots of other LESS files included by the above that aren't
worth listing out. The above two files are the common entry points for usage of
Bootstrap styles.

### JavaScript

Unlike the LESS sources, the javascript modules each represent a feature set
that you may or may not want to include in your site. These files are
typically hand-picked based on the needs of your site. Please check the
Bootstrap documentation for info on which of these modules depends on others.

 * `js/bootstrap-transition.js`
 * `js/bootstrap-alert.js`
 * `js/bootstrap-modal.js`
 * `js/bootstrap-dropdown.js`
 * `js/bootstrap-scrollspy.js`
 * `js/bootstrap-tab.js`
 * `js/bootstrap-tooltip.js`
 * `js/bootstrap-popover.js`
 * `js/bootstrap-button.js`
 * `js/bootstrap-collapse.js`
 * `js/bootstrap-carousel.js`
 * `js/bootstrap-typeahead.js`
 * `js/bootstrap-affix.js`

### Images

Icons by Glyphicons. Include both of these files if you expect to use any
Bootstrap-packaged icons.

 * `img/glyphicons-halflings-white.png`
 * `img/glyphicons-halflings.png`

## Plain Usage

If you're not using an asset manager, you can just include them as usual in
your site templates.

```html
{% load staticfiles %}
...
<script type="text/javascript" src="{% static 'js/bootstrap-transition.js' %}"></script>
...
```

## Usage with an asset managemer pipeline

Of course I recommend you not go plain, and instead use an asset manager that
helps with the filtering, concatenating, minification, and other processing of
your static assets. One such manager is
[django-pipeline](https://github.com/cyberdelia/django-pipeline).

Follow the setup instructions for django-pipeline, define asset groups which
provide Twitter Bootstrap, and then include them in your templates.

```python
# settings.py

PIPELINE_CSS = {
    ...
    'bootstrap': {
        'source_filenames': (
            'less/bootstrap.less',
            'less/responsive.less'
        ),
        'output_filename': 'css/b.css',
        'extra_context': {
            'media': 'screen,projection',
        },
    },
    ...
}

PIPELINE_JS = {
    ...
    'bootstrap': {
        'source_filenames': (
          'js/bootstrap-transition.js',
          'js/bootstrap-alert.js',
          'js/bootstrap-modal.js',
          'js/bootstrap-dropdown.js',
          'js/bootstrap-scrollspy.js',
          'js/bootstrap-tab.js',
          'js/bootstrap-tooltip.js',
          'js/bootstrap-popover.js',
          'js/bootstrap-button.js',
          'js/bootstrap-collapse.js',
          'js/bootstrap-carousel.js',
          'js/bootstrap-typeahead.js',
          'js/bootstrap-affix.js',
        ),
        'output_filename': 'js/b.js',
    },
    ...
}

```

Of course you need to
[set up a LESS compiler](http://django-pipeline.readthedocs.org/en/latest/compilers.html#less-compiler)
for pipeline to use when processing those styles.

```html
...
{% load compressed %}
...
<head>
  ...
  {% compressed_css 'bootstrap' %}
  ...
</head>
<body>
  ...
  {% compressed_js 'bootstrap' %}
  ...
</body>
</html>
```

That's it. Enjoy!
