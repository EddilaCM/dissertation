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
    training = actData.sample(frac=0.3,axis=0)
    # training = training.set_index('user')
    # training.to_csv('../dataset/training_laogo_log.csv')
    # print actData.columns
    for index1,all_row in actData.iterrows():
        for index2,train_row in training.iterrows():
            if all_row['time_second']==train_row['time_second']:
                actData.drop(actData.index[index1],inplace=True)
    print len(actData)



if __name__ == '__main__':
    get_random_item()