# -*- coding:utf-8 -*-
# __author__ = 'cm'
import csv
import pandas as pd


def mapdf(df_arg):
    df_arg_mapping = {label:idx for idx,label in enumerate(set(df_arg))}
    for idx,label in enumerate(set(df_arg)):
        print label,idx
    df_arg = df_arg.map(df_arg_mapping)
    return df_arg


def pandasOneHotCoding(odata,classtype):
    # ['Job_name', 'class_one', 'class_two', 'class_three', 'job_company', 'low_salary', 'low _year', 'job_edu', 'job_area', 'second_time']
    #  class_one     job_company low _salary  low _year  job_edu job_area  second_time
    odata.drop(['low _salary','low _year','second_time'],axis=1,inplace=False)
    df = odata
    # 地区映射
    # job_area_mapping = {label:idx for idx,label in enumerate(set(df['job_area']))}
    # df['job_area'] = df['job_area'].map(job_area_mapping)
    # if classtype==1:
    #     df['class_one'] = mapdf(df['class_one'])
    # elif classtype==2:
    #     df['class_two'] = mapdf(df['class_two'])
    # elif classtype==3:
    #     df['class_three'] = mapdf(df['class_three'])
    # 最低学历
    # job_edu_mapping ={u'不限':0,u'大专':1,u'本科':2,u'博士':3,u'硕士':4}
    # df['job_edu'] = df['job_edu'].map(job_edu_mapping)
    df['job_edu'] = mapdf(df['job_edu'])
    data = pd.get_dummies(df)
    data.to_csv('../dataset/newjobclass'+str(classtype)+'2.csv')
    return pd.get_dummies(df)


if __name__ == '__main__':
    # open file named job.csv
    readfilename = '../dataset/real_job.csv'
    odata =pd.read_csv(readfilename)
    odata = odata.set_index('Job_name')
    # print 'odata:',odata
    # 类别数据
    classType = 1
    # del odata['Job_name']
    if classType==1:
        odata.drop(['class_two','class_three'],axis=1,inplace=True)
    elif classType==2:
        odata.drop(['class_one','class_three'],axis=1,inplace=True)
    elif classType==3:
        odata.drop(['class_one','class_two'],axis=1,inplace=True)
    # print 'data:',odata
    pandasOneHotCoding(odata,classType)


# 离散特征的编码分为两种情况：
#                         1.离散特征的取值之间没有大小的意义，比如color：[rea,green],那么久使用one-hot编码
#                         2.离散特征的取值有大小意义，比如size：[X,XL,XXL]，可以使用数值的映射{X:1,XL:2,XXL:3}