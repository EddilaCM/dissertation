# -*- coding:utf-8 -*-
# __author__ = 'cm'
import csv
import pandas as pd
import numpy as np
from sklearn_pandas import DataFrameMapper
from sklearn.preprocessing import OneHotEncoder


# 只能处理int 类型输入的数据
# def one_hot_encoding(dataArr):
#     # one-hot编码过程
#     enc = OneHotEncoder()
#     enc.fit(dataArr)
#     data_hoted = enc.transform(dataArr).toarray()
#     return data_hoted


def mapdf(df_arg):
    df_arg_mapping = {label:idx for idx,label in enumerate(set(df_arg))}
    df_arg = df_arg.map(df_arg_mapping)
    return df_arg


def pandasOneHotCoding(dataArr,classtype):
    # ['Job_name', 'class_one', 'class_two', 'class_three', 'job_company', 'low_salary', 'low _year', 'job_edu', 'job_area', 'second_time']
    # dataArr = dataArr.drop
    df = pd.DataFrame(dataArr)
    df.columns = dataArr[0]
    # 地区映射
    job_area_mapping = {label:idx for idx,label in enumerate(set(df['job_area']))}
    df['job_area'] = df['job_area'].map(job_area_mapping)
    if classtype==1:
        df['class_one'] = mapdf(df['class_one'])
    elif classtype==2:
        df['class_two'] = mapdf(df['class_two'])
    elif classtype==3:
        df['class_two'] = mapdf(df['class_two'])
    # 公司
    df['job_company'] = mapdf(df['job_company'])
    # 最低学历
    df['job_edu'] = mapdf(df['job_edu'])
    data = pd.get_dummies(df)
    data.to_csv('../dataset/jobclass'+str(classtype)+'.csv')
    return pd.get_dummies(df)


if __name__ == '__main__':
    # open file named job.csv
    readfilename = '../dataset/real_job.csv'
    openRfile = open(readfilename,'r')
    reader = csv.reader(openRfile)
    dataArr = []
    # 类别数据
    classType = 1
    i = 0
    for row in reader:
        new_row = [item for item in row]
        dataArr.append(new_row)
        i += 1
    nameArr = dataArr[0]
    print "orginal nameArr:",nameArr
    #去除第一列 即username
    dataArr = np.array(dataArr)
    # arrNoName = map(lambda x:x[1:],dataArr)#去掉第一列（item的名字列）
    noclassArray = map(lambda x:x[4:10],dataArr)
    if classType==1:
        classone = np.array(map(lambda x:x[1],dataArr))
        arrNoName = np.c_[classone,noclassArray]
        del nameArr[0],nameArr[2],nameArr[2]
        # del
        # del nameArr[3]
        # np.delete(nameArr,0,axis=0)
        # np.delete(nameArr,2,axis=0)
        # np.delete(nameArr,3,axis=0)
    elif classType==2:
        classtwo = map(lambda x:x[2],dataArr)
        arrNoName = np.c_[classtwo,noclassArray]
        del nameArr[0]
        del nameArr[1]
        del nameArr[3]
        # np.delete(nameArr,0,axis=0)
        # np.delete(nameArr,1,axis=0)
        # np.delete(nameArr,3,axis=0)
    elif classType==3:
        classthree = np.array(map(lambda x:x[3],dataArr))
        arrNoName = np.np.c_[classthree,noclassArray]
        del nameArr[0]
        del nameArr[1]
        del nameArr[2]
        # np.delete(nameArr,0,axis=0)
        # np.delete(nameArr,1,axis=0)
        # np.delete(nameArr,1,axis=0)
    print 'nameArr',nameArr
    # print 'nameArr[1]',nameArr[1]
    print 'data',arrNoName
    print pandasOneHotCoding(arrNoName,classType)



# 离散特征的编码分为两种情况：
#                         1.离散特征的取值之间没有大小的意义，比如color：[rea,green],那么久使用one-hot编码
#                         2.离散特征的取值有大小意义，比如size：[X,XL,XXL]，可以使用数值的映射{X:1,XL:2,XXL:3}