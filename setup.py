#-*- coding:utf-8 -*-
from setuptools import setup
import django_debug_html_store

short_description = '`django_debug_html_store` is django debug tool.'
long_description = """\
`django_debug_html_store` is django debug tool.

Requirements
------------
* Python 2.5 or later (not support 3.x)
* Django 1.1 or later (Support 1.3 final)
Features
--------
* nothing

Setup
-----
::

   $ easy_install django_debug_html_store
   or
   $ pip install django_debug_html_store

History
-------
0.0.1 (2011-4-18)
~~~~~~~~~~~~~~~~~~
* first release

"""

classifiers = [
    "Development Status :: 1 - Planning",
    "Topic :: Software Development :: Debuggers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Framework :: Django",
]

setup(
    name             = django_debug_html_store.__name__,
    version          = django_debug_html_store.__version__,
    py_modules       = ['django_debug_html_store'],
    description      = description,
    long_description = long_description, 
    author           = django_debug_html_store.__author__,
    author_email     = 'salexkidd@gmail.com',
    url              = 'http://github.com/salexkidd/django-debug_html_store',
    keywords         = 'django, debug, response',
    license          = django_debug_html_store.__license__,
    packages         = ('django_debug_html_store',),
    classifiers      = classifiers,

    )
