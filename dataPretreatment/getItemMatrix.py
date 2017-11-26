# -*- coding:utf-8 -*-
# __author__ = 'cm'
import csv
from sklearn import preprocessing


def one_hot_encoding(dataArr):
    # one-hot编码过程
    enc = preprocessing.OneHotEncoder()
    enc.fit(dataArr)
    data_hoted = enc.transform(dataArr).toarray()
    return data_hoted


if __name__ == '__main__':
    # open file named job.csv
    readfilename = '../dataset/real_job.csv'
    openRfile = open(readfilename,'r')
    reader = csv.reader(openRfile)
    dataArr = []
    i = 0
    for row in reader:
        new_row = [item for item in row]
        dataArr.append(new_row)
        i += 1
    nameArr = dataArr[0]
    print dataArr
    print one_hot_encoding(dataArr)