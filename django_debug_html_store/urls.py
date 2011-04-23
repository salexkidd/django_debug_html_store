"""
django_debug_html_store urls.py
"""

from django.conf.urls.defaults import *

urlpatterns = patterns('django_debug_html_store.views',
                       url('^read_response/$', 'read_response'),
                       url('^read_response/(?P<ip_addr>.+)/$',
                           'read_response'),
                       url('^test/http_response/$', 'ret_test_http_response'),
                       url('^test/redirect_response/$',
                           'ret_test_redirect_response'),
                       )
