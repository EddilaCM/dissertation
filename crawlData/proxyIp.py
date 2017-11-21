__author__ = 'cm'
# -*- coding:utf-8 -*-
import urllib2
import csv
import socket


# get property ip for current url
def getIpList(url):
    socket.setdefaulttimeout(2)
    reader=csv.reader(open('learn_proxy/ips.csv'))
    IPpool=[]
    for row in reader:
        proxy=row[0]+':'+row[1]
        proxy_handler=urllib2.ProxyHandler({"http":proxy})
        opener=urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)
        try:
            html=urllib2.urlopen(url)
            # IPpool.append([row[0],row[1]])
            IPpool.append(proxy)
            # print(IPpool)
        except Exception,e:
            continue
    # print(IPpool)
    return IPpool


def del_ips(ips):
    delips = ['111.76.133.113:808','123.169.86.244:808','122.237.43.119:808','121.226.169.233:808', '183.32.88.152:808','218.64.93.201:808','110.72.182.21:8123','112.85.9.216:808', '61.188.24.232:808']
    for ip in ips:
        for delete in delips:
            if ip == delete:
                ips.remove(ip)
    return ips


if __name__ == '__main__':
    IPArr = getIpList("https://www.lagou.com/")
    after_IPs = del_ips(IPArr)
    f_ip_txt = file('ip.txt','w+')
    for a in after_IPs:
        f_ip_txt.write(a+"\n")
    f_ip_txt.close()
    # ips = file('ip.txt','r')
    # ipPool=[]
    # for ip in ips:
    #     print(ip)
    #     ipPool.append(ip)
    # ips.close()

