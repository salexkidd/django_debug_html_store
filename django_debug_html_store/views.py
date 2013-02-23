#-*- coding:utf-8 -*-
"""
django_debug_html_store views module
"""
from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse, HttpResponseRedirect
import random


def read_response(request, **kwargs):
    """
    Read Debug HTML File or cache data and return response.
    """
    #if settings.DEBUG is False then redirect to "/"
    if not getattr(settings, 'DEBUG', False):
        return HttpResponseRedirect('/')

    #Don't store django_html_store's read_response view's response
    setattr(request, 'do_not_store_response', True)
    store_response = ''

    ip_addr = kwargs.get('ip_addr', request.META['REMOTE_ADDR'])
    debug_store_type = getattr(settings, 'DEBUG_STORE_HTML_STORE_TYPE', None)

    if not debug_store_type in ('file', 'cache'):
        raise Warning('DEBUG_STORE_HTML_STORE_TYPE should be file or cache')

    if debug_store_type == 'file':
        fname = "{}_{}".format(
            getattr(settings, 'DEBUG_STORE_FILE_PREFIX', "debug_store"),
            ip_addr.replace('.', '_'),)

        try:
            store_response = open(fname, 'r').read()

        except Exception as e:
            error_res = 'django_debug_html_store Error: %s' % (e),
            return HttpResponse(error_res, status=200)

    elif debug_store_type == 'cache':
        cache_name = 'DJANGO_HTML_STORE_MIDDLEWARE_CACHE_%s' % (ip_addr)
        cache_str = cache.get(cache_name)

        if cache_str:
            store_response += cache_str

        else:
            return HttpResponse('No cache data.', status=404)

    return HttpResponse(store_response, status=200)


def test_http_response(request, **kwargs):
    """
    test response function (HttpResponse)
    """
    randint = random.randint(1, 10000)
    return HttpResponse('Random int:%s' % (randint), status=200)


def test_redirect_response(request, **kwargs):
    """
    test response function (HttpResponseRedirect)
    """
    return HttpResponseRedirect('http://www.google.com/')
