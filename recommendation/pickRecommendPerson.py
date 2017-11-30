# __author__ = 'cm'
# -*- coding:utf-8 -*-
from numpy import *  #导入numpy的库函数
# import numpy as np  #这个方式使用numpy的函数时，需要以np.开头。
import pandas as pd
import csv
import time


def Date2Second(Date):
        date = time.strptime(Date,"%Y/%m/%d %H:%S")
        return time.mktime(date)


def creatMatrix(data,date_line,time_space):
    peopleArr = []
    user_time = []
    for row in data:
        if row[1] not in peopleArr:
            peopleArr.append(row[1])
    # print peopleArr
    print len(peopleArr)
    for people_now in peopleArr:
        tempTime = []
        for row_t in data:
            if people_now == row_t[1]:
                tempTime.append(Date2Second(row_t[3]))
        user_time.append(sort(tempTime))
    # print user_time
    recommend_people = []
    for person,lastTime in zip(peopleArr,user_time):
        if lastTime[-1]>(date_line-time_space):
            recommend_people.append(person)
    print recommend_people
    pd.DataFrame(recommend_people).to_csv('../dataset/recomendPeople_Lago.csv')
    print len(recommend_people)


# 读取数据文件，返回数据
def readfilereturndataArr(filepath):
    data_1 = []
    open_file = open(filepath,mode='r')
    csv_reader = csv.reader(open_file)
    for row in csv_reader:
        data_1.append(row)
    open_file.close()
    del data_1[0]
    return data_1


def main():
    # 参数设置
    date_line = Date2Second('2014/10/1 0:0')
    time_space = 7*24*60*60
    # 读取数据文件  item,user,active,time
    file_open = '../dataset/(sample)sam_tianchi_2014002_rec_tmall_log.csv'
    data_1 = readfilereturndataArr(file_open)
    creatMatrix(data_1,date_line,time_space)


if __name__ == '__main__':
    main()