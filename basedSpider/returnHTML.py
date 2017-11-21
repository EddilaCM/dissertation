# __author__ = 'Administrator'
# -*- coding:utf-8 -*-
import urllib
import urllib2
import random
# import returnHeader


class ReturnHTML:
    def __init__(self,header,url,IPPool,enable_proxy):
        # self.header = returnHeader.setHeader(User_Agent, Accept, Accept_Charset, Accept_Encoding, Host)
        self.header = header
        self.url=url
        self.IPPool=IPPool
        self.enable_proxy = enable_proxy

    #IP代理池爬取+模仿浏览器
    def IPPool_browser(self):
        req_timeout = 10
        # 代理设置
        proxy = self.IPPool[random.randint(0, len(self.IPPool)-1)]
        # print('this IP:',proxy)
        # 是否使用代理
        enableProxy = self.enable_proxy
        proxy_handler = urllib2.ProxyHandler({"http":"http://%s" % proxy})
        null_proxy_handler = urllib2.ProxyHandler({})
        if enableProxy:
            opener = urllib2.build_opener(proxy_handler,urllib2.HTTPHandler(debuglevel=1))
        else:
            opener = urllib2.build_opener(null_proxy_handler)
        urllib2.install_opener(opener)
        try:
            request = urllib2.Request(self.url, None, self.header)
        except urllib2.URLError,e:
            print(e.reason)
        # 我们知道，HTTPError的父类是URLError，根据编程经验，父类的异常应当写到子类异常的后面，如果子类捕获不到，那么可以捕获父类的异常
        try:
            urllib2.urlopen(request, None, req_timeout)
        except urllib2.URLError,e:
            if hasattr(e,"code"):
                print e.code
        except urllib2.HTTPError,e:
            if hasattr(e,"reason"):
                print e.reason
        response = urllib2.urlopen(request, None, req_timeout)
        html = response.read()
        return html

    def rqsWay_IpPool_Brower(self,request_way,args):
        req_timeout = 10
        proxy = self.IPPool[random.randint(0, len(self.IPPool)-1)]
        proxy_handler = urllib2.ProxyHandler({"http":"http://%s" % proxy})
        null_proxy_handler = urllib2.ProxyHandler({})
        if self.enable_proxy:
            opener = urllib2.build_opener(proxy_handler,urllib2.HTTPHandler(debuglevel=1))
        else:
            opener = urllib2.build_opener(null_proxy_handler)
        urllib2.install_opener(opener)
        data1 = urllib.urlencode(args)
        # data1 = urllib.parse.urlencode(args)
        # print(data1)
        if request_way == "get":
            # get方式的请求直接将参数加在URL的后面
            url = self.url + '?' + data1
            print url
            try:
                request = urllib2.Request(url, None, self.header)
            except urllib2.URLError,e:
                print(e.reason)
            response = urllib2.urlopen(request, None, req_timeout)
        else:
            try:
                request = urllib2.Request(self.url, data1, self.header)
            except urllib2.URLError,e:
                print(e.reason)
            response = urllib2.urlopen(request, None, req_timeout)
        html = response.read()
        return html



