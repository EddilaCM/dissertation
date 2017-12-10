# -*- coding:utf-8 -*-
# __author__ = 'cm'
import pandas as pd
import numpy as np
import random


def getRandomItem(odata,items):
    # [u'user', u'time', u'frequency', u'link', u'time_second', u'year',
       # u'month', u'day', u'hour', u'minutes', u'second', u'link_times']
    print odata.columns
    item_map = map_array(items)
    users = odata['user']
    user_map = map_set_df(users)
    link_times = odata['link_times']
    odata['items']=''
    odata['items_map']=''
    odata['user_map']=user_map
    itemsArr = []
    itemsMapArr = []
    for i,txt in enumerate(np.array(link_times)):
        tempArr = random.sample(items,txt)
        tempArr_map = random.sample(item_map,txt)
        # odata['items'][i]=tempArr
        itemsArr.append(tempArr)
        itemsMapArr.append(tempArr_map)
    odata['items'] = itemsArr
    odata['items_map'] = itemsMapArr
    return odata


def map_set_df(df_arg):
    # 数组
    df_arg_mapping = {label:'U'+str(idx) for idx,label in enumerate(set(df_arg))}
    df_arg = df_arg.map(df_arg_mapping)
    return df_arg


def map_array(array):
    array_end =[]
    for index,label in enumerate(array):
        temp = 'I'+str(index)
        array_end.append(temp)
    return array_end

def getUserItemMatrix(data,items,name):
    # print data
    items =map_array(items)
    Ori_user = data['user_map']
    Ori_item = data['items_map']
    user_item = pd.DataFrame(np.zeros((len(set(Ori_user)),len(items))),index=set(Ori_user),columns=items)
    print user_item
    for user,item1 in zip(np.array(Ori_user),np.array(Ori_item)):
        for i in item1:
            print i,user
            user_item[i][user] = 1
            print user_item[i][user]
    print user_item
    user_item.to_csv('../dataset/logou_classfication/user_item_'+name+'.csv')



if __name__ == '__main__':
    train_file = '../dataset/test/act_lagou_trainingData.csv'
    test_file = '../dataset/test/act_lagou_testData.csv'
    item_file = '../dataset/real_job.csv'
    trainingSet = pd.read_csv(train_file)
    testSet = pd.read_csv(test_file)
    itemAllSet = pd.read_csv(item_file)
    items = np.array(itemAllSet['Job_name'])
    # print trainingSet.index
    # print items
    training = getRandomItem(trainingSet,items)
    testing = getRandomItem(testSet,items)
    getUserItemMatrix(training,items,'training')
    getUserItemMatrix(testing,items,'test')