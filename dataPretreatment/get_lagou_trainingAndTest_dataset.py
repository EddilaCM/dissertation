# -*- coding:utf-8 -*-
# __author__ = 'cm'
import pandas as pd
import numpy as np


def get_random_item():
    itemFile = '../dataset/real_job.csv'
    # Job_name	class_one	class_two	class_three	job_company	low _salary	low _year	job_edu	job_area	second_time
    actionFile = '../dataset/actData.csv'
    # ip	time	frequency	link	time_second	year	month	day	hour	minutes	second	link_times
    itemData = pd.read_csv(itemFile)
    actData = pd.read_csv(actionFile)
    jobs = itemData['Job_name']
    users_row = np.array(actData['user'])
    users_set = set(actData['user'])
    print len(users_row),len(users_set)
    training = actData.sample(frac=0.7,axis=0)
    # 获取train的下标
    train_index = training.index
    #从整个数据中删除train的数据（按行）
    actData.drop(train_index,axis=0,inplace=True)
    print len(actData)
    training = training.set_index('user')
    actData = actData.set_index('user')
    actData.to_csv('../dataset/test/act_lagou_testData.csv')
    training.to_csv('../dataset/test/act_lagou_trainingData.csv')



if __name__ == '__main__':
    get_random_item()