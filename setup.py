# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


setup(
    name="django-bootstrap-less",
    version="3.3.0",
    packages=find_packages(),
    package_data={
        'bootstrap_less': [
            'static/bootstrap_less/fonts/glyphicons-halflings-regular.*',
            'static/bootstrap_less/js/*.js',
            'static/bootstrap_less/less/*.less',
            'static/bootstrap_less/less/mixins/*.less',
        ],
    },

    # metadata for upload to PyPI
    author="Steven Cummings",
    author_email="cummingscs@gmail.com",
    description="Provides a Django app whose static folder contains Bootstrap assets",
    license="MIT",
    keywords="django app staticfiles bootstrap",
    url="https://github.com/estebistec/django-bootstrap-less",
    download_url="http://pypi.python.org/pypi/django-bootstrap-less",
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
