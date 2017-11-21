# __author__ = 'cm'
# -*- coding:utf-8 -*-


class returnHeader:

    # 头部信息
    def setHeader(self,agent, accept, accept_charset, accept_encoding, host):
        self.header = {'User-Agent': self.setAgent(agent),
                       'Accept': self.setAccept(accept),
                       'Accept-Charset': self.setCharset(accept_charset),
                       'Accept_Encoding': self.setEncoding(accept_encoding),
                       'Connection': 'close',
                       'Referer':None,
                       'Host':self.setHost(host)}
        return self.header

    def setAgent(self,arg):
        self.agent = arg
        return self.agent

    def setAccept(self,arg):
        self.accept = arg
        return self.accept

    def setCharset(self,arg):
        self.accept_charset = arg
        return self.accept_charset

    def setEncoding(self,arg):
        self.accept_encoding = arg
        return self.accept_encoding

    def setHost(self,arg):
        self.Host = arg
        return self.Host