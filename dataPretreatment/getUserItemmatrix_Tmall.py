# -*- coding:utf-8 -*-
# __author__ = 'cm'
import pandas as pd
import numpy as np
import time


def Date2Second(Date):
    date = time.strptime(Date,"%Y/%m/%d %H:%M")
    return time.mktime(date)

if __name__ == '__main__':
    # read data file
    Tmall_act_dada_file = '../dataset/(sample)sam_tianchi_2014002_rec_tmall_log.csv'
    # item_id	user_id	action	vtime
    Tmall_act_dada = pd.read_csv(Tmall_act_dada_file)
    oItem = Tmall_act_dada['item_id']
    oUser = Tmall_act_dada['user_id']
    item = set(oItem)
    user = set(oUser)
    m_user = len(user)
    n_item = len(item)
    print m_user, n_item
    user_item = pd.DataFrame(np.zeros((m_user,n_item)),index=user,columns=item)
    for u,i in zip(np.array(oUser),np.array(oItem)):
        print u,i
        user_item[i][u] = int(1)
    user_item.to_csv('../dataset/user_item_Tmall.csv')


