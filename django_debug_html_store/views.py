#-*- coding:utf-8 -*-

"""
Return stored debug response HTML
"""
from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
import random

def read_response(request, **kwargs):
    """
    Read Debug HTML File
    """
    
    if getattr(settings, 'DEBUG'):
        pass
    else:
        return HttpResponseRedirect('/')

    #Don't store read_response view response
    setattr(request, 'NoStoreResponse', True)
    store_res = ''
   
    if kwargs.get('ip_addr'):
        ip_addr = kwargs.get('ip_addr')
    else:
        ip_addr = request.META['REMOTE_ADDR']

    debug_store_type = getattr(settings, 'DEBUG_STORE_HTML_STORETYPE')
    if debug_store_type == 'file':
        html_filename = getattr(settings, 'DEBUG_STORE_HTML_FILE')
        if html_filename is None:
            return response
        
        html_filename+= "_%s" % (ip_addr.replace('.', '_'))

        try:
            store_res = open(html_filename, 'r').read()
            #for l in open(html_filename, 'r').readlines():
            #    store_res += l
        except Exception, e:
            error_res = "django_debug_html_store Error: %s" % (e),
            return HttpResponse(error_res, status=200)
    
    elif debug_store_type == 'cache':

        cache_name = 'DJANGO_HTML_STORE_MIDDLEWARE_CACHE_%s' % (ip_addr)
        cache_str = cache.get(cache_name)
        if cache_str:
            store_res += cache_str
        else:
            return HttpResponse('cache data is None', status=200)

    return HttpResponse(store_res, status=200)

def ret_test_http_response(request, **kwargs):
    """
    test response function (HttpResponse)
    """
    randint = random.randint(1,10000)
    return HttpResponse("Random int:%s" % (randint), status=200)

def ret_test_redirect_response(request, **kwargs):
    """
    test response function (HttpResponseRedirect)
    """
    return HttpResponseRedirect('http://www.google.com/')
