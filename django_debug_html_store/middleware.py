#-*- coding:utf-8 -*-
"""
django_debug_html_store middleware Module

"""

from django.conf import settings
from django.core.cache import cache
import re

try:
    from django.utils.timezone import now
except ImportError:
    from datetime.datetime import now


EXCLUDE_REGEX = "^.+\.(" + 'css|js|ico|jpg|png|gif' + ')$'


class DebugStoreMiddleware(object):
    """
    HTML Store Middleware
    """
    def process_response(self, request, response):
        """
        Catch & Store response to file or cache.
        """
        if hasattr(request, 'do_not_store_response'):
            if request.do_not_store_response:
                return response

        if re.search(EXCLUDE_REGEX, request.path):
            return response

        if not getattr(settings, "DEBUG", False):
            return response

        file_handle = ''
        debug_store_type = None
        ip_addr = request.META['REMOTE_ADDR']

        try:
            debug_store_type = getattr(settings, 'DEBUG_STORE_HTML_STORE_TYPE')

        except Exception:
            msg = "Please Set DEBUG_STORE_HTML_STORE_TYPE to settings.py"
            raise Warning(msg)

        if debug_store_type == 'file':
            """
            Store response to specify `settings.DEBUG_STORE_FILE_PREFIX` file.
            """
            html_filename = getattr(
                settings, 'DEBUG_STORE_FILE_PREFIX', "debug_store")

            if html_filename is None:
                return response

            html_filename += "_%s" % (ip_addr.replace('.', '_'))
            file_handle = open(html_filename, 'w')

        elif debug_store_type == 'cache':
            """
            Store response to Memcached (more than else)
            (Hint: Are you remenber? GoogleAppEngine can't open file.)
            """
            pass

        else:
            return response

        res_str = ''
        if response:
            for l in response:
                res_str += l

        res_str += '\n <!-- django_debug_html_store'
        res_str += '\n Dump to %s date: %s --> ' % (debug_store_type,
                                                    now())
        if debug_store_type == 'file':
            file_handle.write(res_str)
            file_handle.flush()
            file_handle.close()

        elif debug_store_type == 'cache':
            cache_name = 'DJANGO_HTML_STORE_MIDDLEWARE_CACHE_%s' % (ip_addr)
            cache.set(cache_name, res_str, 3600 * 24)

        return response
