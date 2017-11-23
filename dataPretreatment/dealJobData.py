# coding=utf-8
# __author__ = 'cm'
# -*- coding:utf-8 -*-
import csv
import re
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def Date2Second(Date):
        if Date=="job_release_time":
            return "second_time"
        else:
        # date = Date.strftime("%Y-%m-%d %H:%S:%M")
            date = time.strptime(Date,"%Y/%m/%d %H:%M")
            return time.mktime(date)


def timefixed(agr):
    if agr =='job_release_time':
        return agr
    else:
        # print agr
        time_reg_exp = re.compile('\d{1,2}:\d{1,2}')
        tim1 = re.search(r"(\d{4}\/\d{1,2}\/\d{1,2})",agr)
        if tim1:
            return agr+" 00:00"
        else:
            agr1 = time_reg_exp.findall(agr)
            if len(agr1)!=0:
                ms = agr1[0]
            else:
                ms = "00:00"
            return "2017/11/08 "+ms


def deleteJinyan(arg):
    year_reg = re.compile("[\d{1,2}:\d{1,2}]|"+r"'不限'")
    end = year_reg.findall(arg)
    lowYear = 0
    if len(end)!=0:
        lowYear = end[0]
    return lowYear


def areaCut(arg):
    if arg == 'job_area':
        return arg
    else:
        arg = arg.replace('\n','')
        arg1 = arg.decode('gbk')
        area = arg1.split('·')[0]
        area1 = area.decode('utf-8')
        return area1


if __name__ == '__main__':
    # r = '上海·漕宝路'
    # print areaCut(r)
    # print "hhhh",r.decode('utf-8')
    # print timefixed('18:32发布')
    # print timefixed('2017-11-08')
    # read no dealing file
    filename = '../basedSpider/dataFile/laGou_JobList_all20171108.csv'
    csvFile = open(filename,'r')
    reader = csv.reader(csvFile)
    # write new data to a file named job.csv
    saveFile = '../dataset/job.csv'
    wiritcsv = open(saveFile,'wb')
    writer = csv.writer(wiritcsv)
    for row in reader:
        new_row = row
        # time
        new_row[7] = timefixed(row[7])
        seconds = Date2Second(new_row[7])
        new_row[8] = deleteJinyan(row[8])
        areaArr = areaCut(row[10])
        new_row[10] = areaArr
        print new_row[10]
        del new_row[5]
        new_row.append(seconds)
        writer.writerow(new_row)
    wiritcsv.close()
    csvFile.close()