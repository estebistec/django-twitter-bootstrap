# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name="django-twitter-bootstrap",
    version="3.3.0",
    packages=find_packages(),
    package_data={
        'twitter_bootstrap': [
            'static/twitter_bootstrap/fonts/glyphicons-halflings-regular.*',
            'static/twitter_bootstrap/js/*.js',
            'static/twitter_bootstrap/less/*.less',
            'static/twitter_bootstrap/less/mixins/*.less',
        ],
    },

    # metadata for upload to PyPI
    author="Steven Cummings",
    author_email="cummingscs@gmail.com",
    description="Provides a Django app whose static folder contains Bootstrap assets",
    license="MIT",
    keywords="django app staticfiles twitter bootstrap",
    url="https://github.com/estebistec/django-twitter-bootstrap",
    download_url="http://pypi.python.org/pypi/django-twitter-bootstrap",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries',
    ]
)
