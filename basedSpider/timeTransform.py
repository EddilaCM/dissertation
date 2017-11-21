# __author__ = 'cm'
# -*- coding:utf-8 -*-
import time
import datetime


class TimeSwith:
    def __init__(self):
        pass

    def Date2Second(self, Date):
        # date = Date.strftime("%Y-%m-%d %H:%S:%M")
        date = time.strptime(Date,"%Y/%m/%d")
        return time.mktime(date)


date1 = TimeSwith()
print date1.Date2Second('2017/11/06')