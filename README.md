## Overview

This package provides a [Django](https://www.djangoproject.com) app whose
static folder contains the sources of
[Twitter Bootstrap](http://twitter.github.com/bootstrap), nothing more and
nothing less. The un-minified [LESS](http://lesscss.org) and javascript sources
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
pip install django-twitter-bootstrap==3.0.0-rc2
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

Also included are lots of other LESS files included by the above that aren't
worth listing out. The above two files are the common entry points for usage of
Bootstrap styles.

### JavaScript

Unlike the LESS sources, the javascript modules each represent a feature set
that you may or may not want to include in your site. These files are
typically hand-picked based on the needs of your site. Please check the
Bootstrap documentation for info on which of these modules depends on others.

 * `js/transition.js`
 * `js/modal.js`
 * `js/dropdown.js`
 * `js/scrollspy.js`
 * `js/tab.js`
 * `js/tooltip.js`
 * `js/popover.js`
 * `js/alert.js`
 * `js/button.js`
 * `js/collapse.js`
 * `js/carousel.js`
 * `js/affix.js`

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

## Usage with an asset pipeline

Of course I recommend you not go plain, and instead use an asset manager that
helps with the filtering, concatenating, minification, and other processing of
your static assets. One such manager is
[django-pipeline](https://github.com/cyberdelia/django-pipeline).

 * Follow the setup instructions for django-pipeline
 * Define asset groups which provide Twitter Bootstrap
 * Use asset groups in your templates.

```python
# settings.py

PIPELINE_CSS = {
    ...
    'bootstrap': {
        'source_filenames': (
            'less/bootstrap.less',
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
          'js/transition.js',
          'js/modal.js',
          'js/dropdown.js',
          'js/scrollspy.js',
          'js/tab.js',
          'js/tooltip.js',
          'js/popover.js',
          'js/alert.js',
          'js/button.js',
          'js/collapse.js',
          'js/carousel.js',
          'js/affix.js',
        ),
        'output_filename': 'js/b.js',
    },
    ...
}

```

Of course you need to
[set up a LESS compiler](http://django-pipeline.readthedocs.org/en/latest/compilers.html#less-compiler)
for pipeline to use when processing the styles.

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

## Version ranges matching bootstrap versions

As stated above in the goals, versions of this package should match versions of
Bootstrap, where available. This presents something of a problem if and when we
need to make updates to the *packaging* here. We can't just upgrade any of the
three common components of semantic versioning, because those map to versions
of Bootstrap. So, we'll use revisions when needed.

E.g., suppose we have django-twitter-bootstrap 2.2.2 which packages Twitter
Bootstrap 2.2.2. If we need to enhance or fix the packaging, we release it as
revised version 2.2.2-1.

Therefore, if you're getting a packaging for the first time you could specify
it as a very tight range of that target version or no less than the next patch
level version. E.g., target 2.2.2 with `>=2.2.2,<2.2.3`, or `>=2,<2.0.1`.
Each of these captures all revisions to packagings targetting a specific
version of Bootstrap.

Finally, it should be re-iterated that the need for this should be the
exception and versions should generally mirror Bootstrap more directly going
forward.
