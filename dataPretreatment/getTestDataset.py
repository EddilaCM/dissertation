# -*- coding:utf-8 -*-
# __author__ = 'cm'
import pandas as pd
import numpy as np
import json


if __name__ == '__main__':
    testfilename = '../dataset/(sample)sam_tianchi_2014003_rec_tmall_test.csv'
    # item_id	rater_uid	feedback	gmt_create	rate_pic_url
    oData = pd.read_csv(testfilename)
    user = oData['rater_uid']
    item = oData['item_id']
    all_user = set(user)
    # print all_user
    all_user_info = {}
    for dict_user in all_user:
        all_user_info[dict_user]=[]
    # print all_user_info
    for u,i in zip(np.array(user),np.array(item)):
        all_user_info[u].append(i)
        # print all_user_info[u]
    # print all_user_info
    for k in all_user_info:
        print k,all_user_info[k]
    json_all_user_info = json.dumps(all_user_info)
    fileObject = open('../dataset/all_user_info_test.json','w')
    fileObject.write(json_all_user_info)
    fileObject.close()

