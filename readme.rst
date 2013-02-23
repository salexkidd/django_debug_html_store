======================================================================
django_debug_html_store by salexkidd (http://twitter.com/salexkidd)
======================================================================

.. toctree::

Introduction
____________
django_debug_html_store is a Django debug tool.

Take Django's HttpResponse and dump to file or cache.

And Developer can browse a stored response.

About
_____
With the Django error page is very powerful.

But, it might not be able to read the error page.

Example

* You can brose other developers (or debugger) normal and error response.
* When you construct OpenSocial site, can't retrieve normal and error response.
* Whem you construct Restful API, can't retrieve normal and error response.

How to install
______________

* Download django_debug_html_store
* Set Debug flag to settings.py
* Put the middleware to MIDDLEWARE_CLASS
* Put the url setting to urls.py

``Set Debug flag to settings.py``
---------------------------------
django_debug_html_store require DEBUG flag.

Please put DEBUG flag to Django's settings.py

::

    DEBUG = True
    ...

Put middleware to MIDDLEWARE_CLASS
-------------------------------------------
Please put 'django_debug_html_store.middleware.DebugStoreMiddleware' to settings.MIDDLEWARE_CLASS, Like this.

::

    MIDDLEWARE_CLASSES = (
        'django_debug_html_store.middleware.DebugStoreMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        ...
    )

.. warning::
 You should be put under the 'django.middleware.gzip.GZipMiddleware'.


Put the url setting to urls.py
------------------------------
Please put (r'^debug_response_html/', include('django_debug_html_store.urls')) to project's urls.py
::

    urlpatterns = patterns('',
                           (r'^hogehoge/', include('hogehoge.foo.urls')),
                           (r'^debug_response_html/', include('django_debug_html_store.urls')),
                           ...
    )

Testing django_debug_html_store
_______________________________
After install, you can run the test.

``Browse test view``
--------------------
Please browse "http://[Project URL]/debug_response_html/ret_test_http_response/"
you can see random number.

``Browse stored response html``
-------------------------------
Please browse "http://[Project URL]/debug_response_html/read_response/"
You can see same random number.

``Browse someones response``
----------------------------
Please browse http://[Project URL]/debug_response_html/read_response/[IP Address]/


SETTING ATTR
____________
+----------------------+------------------------------+
| Settings Attr name   | Description                  |
+======================+==============================+


LICENSE
____________

django_debug_html_store is released under the MIT License.
