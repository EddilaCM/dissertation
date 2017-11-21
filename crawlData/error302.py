# -*- coding: utf-8 -*-
#encoding=utf-8
#Filename:states_code.py  
import urllib2


class RedirctHandler(urllib2.HTTPRedirectHandler):
#   """docstring for RedirctHandler"""
    def http_error_301(self, req, fp, code, msg, headers):
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        pass


def getUnRedirectUrl(url,timeout=10):
    req = urllib2.Request(url)
    debug_handler = urllib2.HTTPHandler(debuglevel = 1)
    opener = urllib2.build_opener(debug_handler, RedirctHandler)
    html = None
    response = None
    try:
        response = opener.open(url,timeout=timeout)
        html = response.read()
    except urllib2.URLError as e:
        if hasattr(e, 'code'):
            error_info = e.code
        elif hasattr(e, 'reason'):
            error_info = e.reason
    finally:
        if response:
            response.close()
            if html:
                return html
            else:
                return error_info
html = getUnRedirectUrl('https://www.lagou.com/')