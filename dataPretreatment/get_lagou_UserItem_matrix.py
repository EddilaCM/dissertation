# -*- coding:utf-8 -*-
# __author__ = 'cm'
import pandas as pd
import numpy as np


def getMatrix(odata):
    users = odata['user']
    print len(np.array(users)),len(set(users))


if __name__ == '__main__':
    train_file = '../dataset/test/act_lagou_trainingData.csv'
    test_file = '../dataset/test/act_lagou_testData.csv'
    trainingSet = pd.read_csv(train_file)
    testSet = pd.read_csv(test_file)
    getMatrix(trainingSet)
    # getMatrix(testSet)