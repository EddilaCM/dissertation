# -*- coding:utf-8 -*-
# __author__ = 'cm'
import pandas as pd
import numpy as np


if __name__ == '__main__':
    arr = [1,2,3,4,5]
    # del arr[0,1]
    print arr
    df=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8],"C":[1,1,1,1]})
    # user_item = pd.DataFrame(np.arange(12).reshape(3,4),index=['a','b','c'],columns=['A','B','C','D'])
    # print user_item
    # print user_item['A']['a']