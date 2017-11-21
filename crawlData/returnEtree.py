# __author__ = 'cm'
# -*- coding:utf-8 -*-
import urllib
import urllib2
import random
from lxml import etree
import cookielib


# 仿浏览器得到HTML,返回节点树
def header_browser(enable_proxy, url_pool, url, agent, accept, accept_charset, accept_encoding, host):
    header = {'User-Agent': agent, 'Accept': accept, 'Accept-Charset': accept_charset, 'Accept_Encoding': accept_encoding, 'Connection': 'close', 'Referer':None , 'Host':host}
    req_timeout = 10
    # 代理设置
    proxy = url_pool[random.randint(0, len(url_pool)-1)]
    # print('this IP:',proxy)
    # 是否使用代理
    enableProxy = enable_proxy
    proxy_handler = urllib2.ProxyHandler({"http":"http://%s" % proxy})
    null_proxy_handler = urllib2.ProxyHandler({})
    if enableProxy:
        opener = urllib2.build_opener(proxy_handler,urllib2.HTTPHandler(debuglevel=1))
    else:
        opener = urllib2.build_opener(null_proxy_handler)
    urllib2.install_opener(opener)
    try:
        request = urllib2.Request(url, None, header)
    except urllib2.URLError,e:
        print(e.reason)
    # 我们知道，HTTPError的父类是URLError，根据编程经验，父类的异常应当写到子类异常的后面，如果子类捕获不到，那么可以捕获父类的异常
    try:
        urllib2.urlopen(request, None, req_timeout)
    except urllib2.URLError,e:
        print(e.code)
    except urllib2.HTTPError,e:
        print(e.reason)
    else:
        response = urllib2.urlopen(request, None, req_timeout)
    html = response.read()
    # print(html)
    my_etree = etree.HTML(html)
    return my_etree


# url带参数-get请求
def header_browser1(enable_proxy, url_pool, args, url, agent, accept, accept_charset, accept_encoding, host):
    header = {'User-Agent': agent, 'Accept': accept, 'Accept-Charset': accept_charset, 'Accept_Encoding': accept_encoding, 'Connection': 'close', 'Referer':None , 'Host':host}
    req_timeout = 10
    # 代理意见
    proxy = url_pool[random.randint(0,len(url_pool)-1)]
    print('this IP:',proxy)
    # 是否使用代理
    enable_proxy = enable_proxy
    proxy_handler = urllib2.ProxyHandler({"http":"http://%s" % proxy})
    null_proxy_handler = urllib2.ProxyHandler({})
    if enable_proxy:
        opener = urllib2.build_opener(proxy_handler,urllib2.HTTPHandler(debuglevel=1))
    else:
        opener = urllib2.build_opener(null_proxy_handler)
    urllib2.install_opener(opener)
    data1 = urllib2.urlencode(args)
    # get方式的请求直接将参数加在URL的后面
    url = url + '?' + data1
    print url
    try:
        request = urllib2.Request(url, None, header)
    except urllib2.URLError,e:
        print(e.reason)
    response = urllib2.urlopen(request, None, timeout=None)
    html = response.read()
    # print html
    my_etree = etree.HTML(html)
    # print my_etree
    return my_etree
    request.close()


# url带参数-post请求
def header_browser2(enable_proxy, url_pool, args, url, agent, accept, accept_charset, accept_encoding, host):
    header = {'User-Agent': agent, 'Accept': accept, 'Accept-Charset': accept_charset, 'Accept_Encoding': accept_encoding, 'Connection': 'close', 'Referer':None , 'Host':host}
    req_timeout = 10
    # 代理意见
    proxy = url_pool[random.randint(0,len(url_pool)-1)]
    print('this IP:',proxy)
    # 是否使用代理
    enable_proxy = enable_proxy
    proxy_handler = urllib2.ProxyHandler({"http":"http://%s" % proxy})
    null_proxy_handler = urllib2.ProxyHandler({})
    if enable_proxy:
        opener = urllib2.build_opener(proxy_handler,urllib2.HTTPHandler(debuglevel=1))
    else:
        opener = urllib2.build_opener(null_proxy_handler)
    urllib2.install_opener(opener)
    data1 = urllib.urlencode(args)
    try:
        request = urllib2.Request(url, data1, header)
    except urllib2.URLError,e:
        print(e.reason)
    response = urllib2.urlopen(request, None, req_timeout)
    html = response.read()
    # print html
    my_etree = etree.HTML(html)
    # print my_etree
    return my_etree
    request.close()


# 模仿浏览器获取，不带url_pool,带cookie
def header_browser_cookie(loginUrl, url, agent, accept, accept_charset, accept_encoding, host):
    header = {'User-Agent': agent, 'Accept': accept, 'Accept-Charset': accept_charset, 'Accept_Encoding': accept_encoding, 'Connection': 'close', 'Referer':None , 'Host':host}
    req_timeout = 10
    # # 申明一个CookieJar对象实例来保存cookie
    # cookie = cookielib.CookieJar()
    # # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    # handler = urllib2.HTTPCookieProcessor(cookie)
    # # 通话handler来构建opener
    # opener = urllib2.build_opener(handler)
    # response = opener.open(url)
    filename = 'cookie.txt'
    #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    cookie = cookielib.MozillaCookieJar(filename)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    postdata = urllib.urlencode({
                'stuid':'201200131012',
                'pwd':'23342321'
            })
    #登录教务系统的URL
    # loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
    login_Url = loginUrl
    #模拟登录，并把cookie保存到变量
    result = opener.open(login_Url,postdata)
    #保存cookie到cookie.txt中
    cookie.save(ignore_discard=True, ignore_expires=True)
    #利用cookie请求访问另一个网址，此网址是成绩查询网址
    # gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
    gradeUrl = url
    #请求访问成绩查询网址
    result = opener.open(gradeUrl)
    html = result.read()
    my_etree = etree.HTML(html)
    return my_etree



# 模仿浏览器获取，不带url_pool
def header_browser_nourl_pool(url, agent, accept, accept_charset, accept_encoding, host):
    header = {'User-Agent': agent, 'Accept': accept, 'Accept-Charset': accept_charset, 'Accept_Encoding': accept_encoding, 'Connection': 'close', 'Referer':None , 'Host':host}
    req_timeout = 10
    try:
        req = urllib2.Request(url, None, header)
    except urllib2.URLError,e:
        print(e.reason)
    resq = urllib2.urlopen(req, None, req_timeout)
    html = resq.read()
    # print html
    my_etree = etree.HTML(html)
    # print my_etree
    return my_etree

