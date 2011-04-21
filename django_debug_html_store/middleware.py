#-*- coding:utf-8 -*-

"""
django_debug_html_store
"""

from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse, HttpResponseRedirect
import types
import logging
import re
from datetime import datetime

logger = logging.getLogger('')

EXCLUDE_REGEX = "^.+\.(" + 'css|js|ico|jpg|png|gif' + ')$'

class HtmlStoreMiddleware(object):
    def process_response(self, request, response):
        """
        Catch & Store response to file or cache.
        """
        if hasattr(request, 'NoStoreResponse'):
            if request.NoStoreResponse == True:
                return response

        if re.search(EXCLUDE_REGEX, request.path):            
            return response

        #Check DEBUG Flg
        try:
            if hasattr(settings, 'DEBUG') is False or \
                    settings.DEBUG != True:
                raise
        except:
            return response

        ip_addr = request.META['REMOTE_ADDR']
        file_handle = ''

        debug_store_type = None
        if hasattr(settings, 'DEBUG_STORE_HTML_STORETYPE'):
            debug_store_type = getattr(settings, 'DEBUG_STORE_HTML_STORETYPE')
        
        if debug_store_type == 'file':
            """
            Store response to specify `settings.DEBUG_STORE_HTML_FILE` file.
            """
            html_filename = getattr(settings, 'DEBUG_STORE_HTML_FILE')
            if html_filename is None:
                return response

            html_filename+= "_%s" % (ip_addr.replace('.', '_'))
            file_handle = open(html_filename, 'w')

        elif debug_store_type == 'cache':
            """
            Store response to Memcached (more than else)
            (Hint: GoogleAppEngine are can't open file.)
            """
            pass
        else:
            return response
        
        res_str = ''
        if response:
            for l in response:
                res_str+= l;
        
        res_str+= '\n <!-- django_debug_html_store'
        res_str+= '\n Dump to %s date: %s --> ' % (debug_store_type, datetime.now())
        if debug_store_type == 'file':
            file_handle.write(res_str)
            file_handle.flush()
            file_handle.close()

        elif debug_store_type == 'cache':
            cache_name = 'DJANGO_HTML_STORE_MIDDLEWARE_CACHE_%s' % (ip_addr)
            cache.set(cache_name, res_str, 3600*24)

        return response
