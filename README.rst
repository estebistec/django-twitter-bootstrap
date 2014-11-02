.. image:: https://pypip.in/v/django-twitter-bootstrap/badge.png
    :target: https://pypi.python.org/pypi/django-twitter-bootstrap/
    :alt: Latest Version

.. image:: https://pypip.in/d/django-twitter-bootstrap/badge.png
    :target: https://pypi.python.org/pypi/django-twitter-bootstrap/
    :alt: Downloads

Overview
========

This package provides a `Django <https://www.djangoproject.com>`_ app whose static folder contains
the sources of `Bootstrap <http://getbootstrap.com>`_, nothing more and nothing
less. The un-minified `LESS <http://lesscss.org>`_ and javascript sources are included to be
integrated into your Django site as you see fit. If you simply want to use the minified CSS and JS
files provided by the Bootstrap project, you probably don't need this anyway.

Further goals of this project include:

- To include Bootstrap as a git submodule, so as to include specific release tags and avoid the
  mess of managing a copy of Bootstrap.
- To provide versions that mirror Bootstrap releases going forward.

And that's it! Bootstrap pre-packaged for Django.

I found that other similar projects:

- Did not keep up with recent versions of Bootstrap.
- Simply made a copy of the Bootstrap sources, messy and unnecessary.
- Tied the packaging to their own clever template tags or other Django components. You should have
  your choice of these things apart from this packaging.

Setup
=====

**NOTE** The paths of the included bootstrap assets have now been namespaced within the app's
``static`` folder. The ``less`` and ``js`` folders now reside within a ``twitter_bootstrap``
folder.

First, install the app::

    pip install django-twitter-bootstrap==3.3.0

Then include it in your Django project::

    # settings.py:

    INSTALLED_APPS = (
        ...
        'twitter_bootstrap',
        ...
    )

This also assumes you haven't removed ``django.contrib.staticfiles.finders.AppDirectoriesFinder``
from the ``STATICFILES_FINDERS`` config setting.

Provided staticfiles
====================

Of course what's provided is just Bootstrap, but more specifically...

glyphicons
----------

These don't need to be specified or configured in your project, but they are included all the
same.

- ``twitter_bootstrap/fonts/glyphicons-halflings-regular.eot``
- ``twitter_bootstrap/fonts/glyphicons-halflings-regular.svg``
- ``twitter_bootstrap/fonts/glyphicons-halflings-regular.ttf``
- ``twitter_bootstrap/fonts/glyphicons-halflings-regular.woff``

LESS
----

- ``twitter_bootstrap/less/bootstrap.less``

Also included are lots of other LESS files included by the above that aren't worth listing out.
The above file is the common entry point for usage of Bootstrap styles.

JavaScript
----------

Unlike the LESS sources, the javascript modules each represent a feature set
that you may or may not want to include in your site. These files are
typically hand-picked based on the needs of your site. Please check the
Bootstrap documentation for info on which of these modules depends on others.

- ``twitter_bootstrap/js/transition.js``
- ``twitter_bootstrap/js/modal.js``
- ``twitter_bootstrap/js/dropdown.js``
- ``twitter_bootstrap/js/scrollspy.js``
- ``twitter_bootstrap/js/tab.js``
- ``twitter_bootstrap/js/tooltip.js``
- ``twitter_bootstrap/js/popover.js``
- ``twitter_bootstrap/js/alert.js``
- ``twitter_bootstrap/js/button.js``
- ``twitter_bootstrap/js/collapse.js``
- ``twitter_bootstrap/js/carousel.js``
- ``twitter_bootstrap/js/affix.js``

Plain Usage
===========

If you're not using an asset manager, you can just include them as usual in your site templates::

    {% load staticfiles %}
    ...
    <script type="text/javascript" src="{% static 'twitter_bootstrap/js/transition.js' %}"></script>
    ...

Usage with an asset pipeline
============================

Of course I recommend you not go plain, and instead use an asset manager that helps with the
filtering, concatenating, minification, and other processing of your static assets. One such
manager is `django-pipeline <https://github.com/cyberdelia/django-pipeline>`_.

- Follow the setup instructions for django-pipeline
- Define asset groups which provide Bootstrap
- Use asset groups in your templates.

Configuration
-------------

Create asset groups including the bootstrap LESS and Javascript you want to include::

    # settings.py

    PIPELINE_CSS = {
        ...
        'bootstrap': {
            'source_filenames': (
                'twitter_bootstrap/less/bootstrap.less',
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
              'twitter_bootstrap/js/transition.js',
              'twitter_bootstrap/js/modal.js',
              'twitter_bootstrap/js/dropdown.js',
              'twitter_bootstrap/js/scrollspy.js',
              'twitter_bootstrap/js/tab.js',
              'twitter_bootstrap/js/tooltip.js',
              'twitter_bootstrap/js/popover.js',
              'twitter_bootstrap/js/alert.js',
              'twitter_bootstrap/js/button.js',
              'twitter_bootstrap/js/collapse.js',
              'twitter_bootstrap/js/carousel.js',
              'twitter_bootstrap/js/affix.js',
            ),
            'output_filename': 'js/b.js',
        },
        ...
    }

Of course you need to set up a
`LESS compiler <http://django-pipeline.readthedocs.org/en/latest/compilers.html#less-compiler>`_
for pipeline to use when processing the styles::

    # settings.py

    PIPELINE_COMPILERS = (
        'pipeline.compilers.less.LessCompiler',
    )

Then, in the
`PIPELINE_LESS_ARGUMENTS <http://django-pipeline.readthedocs.org/en/latest/compilers.html#pipeline-less-arguments>`_
setting, supply an ``--include`` option which tells ``lessc`` where bootstrap LESS sources and any
of your own live::

    # settings.py

    import os

    # TODO update this to reflect where your settings live relative to the project root
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    my_app_less = os.path.join(BASE_DIR, 'my_app', 'static', 'less')

    # For apps outside of your project, it's simpler to import them to find their root folders
    import twitter_bootstrap
    bootstrap_less = os.path.join(os.path.dirname(twitter_bootstrap.__file__), 'static', 'less')

    PIPELINE_LESS_ARGUMENTS = u'--include-path={}'.format(os.pathsep.join([bootstrap_less, my_app_less]))

Please note that for any LESS sources outside of your project root, usually these are installed
Django packages, it is simpler to import the package and determine the package root from the
import module's ``__file__`` attribute.

Template setup
--------------

A sample Django template using the assets::

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

That's it. Enjoy!

Version ranges matching bootstrap versions
==========================================

As stated above in the goals, versions of this package should match versions of Bootstrap, where
available. This presents something of a problem if and when we need to make updates to the
*packaging* here. We can't just upgrade any of the three common components of semantic versioning,
because those map to versions of Bootstrap. So, we'll use revisions when needed.

E.g., suppose we have django-twitter-bootstrap 3.2.0 which packages Bootstrap 3.2.0. If we
need to enhance or fix the packaging, we release it as revised version 3.2.0-1.

Therefore, if you're getting a packaging for the first time you could specify it as a very tight
range of that target version or no less than the next patch level version. E.g., target 3.2.0 with
``>=3.2.0,<3.2.1``. Each of these captures all revisions to packagings targeting a specific version
of Bootstrap.

Finally, it should be re-iterated that the need for this should be the exception and versions
should generally mirror Bootstrap more directly going forward.
