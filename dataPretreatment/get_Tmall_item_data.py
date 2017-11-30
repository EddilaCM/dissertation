# -*- coding:utf-8 -*-
# __author__ = 'cm'
# Tmall-product-data deal
import pandas as pd


def pandas_one_hot_encoding(odata):
    data = pd.get_dummies(odata)
    return data


if __name__ == '__main__':
    TmallFileName = '../dataset/(sample)sam_tianchi_2014001_rec_tmall_product.csv'
    data_Tmall_product = pd.read_csv(TmallFileName)
    data_Tmall_product = data_Tmall_product.set_index('item_id')
    Tmall_data = pandas_one_hot_encoding(data_Tmall_product)
    Tmall_data.to_csv('../dataset/data_Tmall_product.csv')