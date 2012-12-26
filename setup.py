# -*- coding: utf-8 -*-


import os

from setuptools import setup, find_packages


README_PATH = os.path.join(os.path.dirname(__file__), 'README.md')


setup(
    name="django-twitter-bootstrap",
    version="2.2.2-1",
    packages=find_packages(),
    package_data={
        'twitter_bootstrap': [
            'static/img/*.png',
            'static/js/bootstrap-*.js',
            'static/less/*.less',
        ],
    },

    # metadata for upload to PyPI
    author="Steven Cummings",
    author_email="cummingscs@gmail.com",
    description="Provides a Django app whose static folder contains Twitter Bootstrap assets",
    long_description=open(README_PATH).read(),
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
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
    ]
)
