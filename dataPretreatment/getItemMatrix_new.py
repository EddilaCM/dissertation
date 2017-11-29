# -*- coding:utf-8 -*-
# __author__ = 'cm'
import csv
import pandas as pd


def mapdf(df_arg):
    df_arg_mapping = {label:idx for idx,label in enumerate(set(df_arg))}
    df_arg = df_arg.map(df_arg_mapping)
    return df_arg


def pandasOneHotCoding(odata,classtype):
    # ['Job_name', 'class_one', 'class_two', 'class_three', 'job_company', 'low_salary', 'low _year', 'job_edu', 'job_area', 'second_time']
    odata.drop(['low _year','second_time'],axis=1,inplace=False)
    # print odata
    # cols = odata.cloumns
    # df = pd.DataFrame(odata)
    df = odata
    # df.columns = cols
    # 地区映射
    # job_area_mapping = {label:idx for idx,label in enumerate(set(df['job_area']))}
    # df['job_area'] = df['job_area'].map(job_area_mapping)
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
      # 最低工资
    df['low_salary'] = mapdf(df['low_salary'])
    data = pd.get_dummies(df)
    data.to_csv('../dataset/newjobclass'+str(classtype)+'.csv')
    return pd.get_dummies(df)


if __name__ == '__main__':
    # open file named job.csv
    readfilename = '../dataset/real_job.csv'
    odata =pd.read_csv(readfilename)
    # print 'odata:',odata
    # 类别数据
    classType = 1
    del odata['Job_name']
    if classType==1:
        odata.drop(['class_two','class_three'],axis=1,inplace=True)
    elif classType==2:
        odata.drop(['class_one','class_three'],axis=1,inplace=True)
    elif classType==3:
        odata.drop(['class_two','class_three'],axis=1,inplace=True)
    # print 'data:',odata
    print pandasOneHotCoding(odata,classType)


# 离散特征的编码分为两种情况：
#                         1.离散特征的取值之间没有大小的意义，比如color：[rea,green],那么久使用one-hot编码
#                         2.离散特征的取值有大小意义，比如size：[X,XL,XXL]，可以使用数值的映射{X:1,XL:2,XXL:3}