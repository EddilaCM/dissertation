# __author__ = 'cm'
# -*- coding:utf-8 -*-
import pickRecommendPerson
import numpy as np
import math


def buliduser_itemMatrix():
    # 读取数据文件  item,user,active,time
    file_open = '../dataset/(sample)sam_tianchi_2014002_rec_tmall_log.csv'
    originData = pickRecommendPerson.readfilereturndataArr(file_open)
    userArr = []
    itemArr = []
    for row in originData:
        if row[0] not in itemArr:
            itemArr.append(row[0])
        if row[1] not in userArr:
            userArr.append(row[1])
    m = len(userArr)
    n = len(itemArr)
    user_itemArr = np.zeros([m,n])
    for i,user in zip(range(0,m,1),userArr):
        for j,item in zip(range(0,n,1),itemArr):
            for Row in originData:
                if Row[1] == user:
                    if Row[0] == item:
                        user_itemArr[i,j] = 1
    return user_itemArr


def itemSimilarity(user_itemArr,i1,i2,computeWay):
    #列计算，返回两个item的相似度
    # a[:,1]---去矩阵的某一列
    # 共现
    i1Arr = user_itemArr[:,i1]
    i2Arr = user_itemArr[:,i2]
    # 计算均值
    I1_yiba = sum(i1Arr)/len(i1Arr)
    I2_yiba = sum(i2Arr)/len(i2Arr)
    # 计算共同评过分的项目
    coI1 = []
    coI2 = []
    for i1,i2 in zip(i1Arr,i2Arr):
        if i1!=0 and i2!=0:
            coI1.append(i1)
            coI2.append(i2)
    gradedI1 = []; gradedI2 = []
    for U1,U2 in zip(i1Arr,i2Arr):
        if U1 !=0:
            gradedI1.append(U1)
        if U2 != 0:
            gradedI2.append(U2)
    if computeWay =="gongxian":
       tempSemiNum = 0
       for I1,I2 in zip(i1Arr,i2Arr):
           if I1!=0 and I2!=0:
               tempSemiNum += 1
       coOcurrenceRate = tempSemiNum/len(i2Arr)
       return coOcurrenceRate
    elif computeWay == "cosine":
        I1_len = math.sqrt(sum([i*i for i in i1Arr]))
        I2_len = math.sqrt(sum([j*j for j in i2Arr]))
        IJ = sum([i*j for i,j in zip(i1Arr,i2Arr)])
        sim_I1I2_cosine =  IJ/(I1_len*I2_len)
        return sim_I1I2_cosine
    elif computeWay == "adjustedcosine":
        #与pearson的区别：修正的cosine 分母是user ij 各自评过分的项;pearson 的分母是共同评分的项，分子都是共同评分的项

        U1_len = math.sqrt(sum([(i-I1_yiba)*(i-I1_yiba) for i in gradedI1]))
        U2_len = math.sqrt(sum([(j-I2_yiba)*(j-I2_yiba) for j in gradedI2]))
        U1_U2 = sum([(i-I1_yiba)*(j-I2_yiba) for i,j in zip(coI1,coI2)])
        sim_U1U2_cosine = U1_U2/(U1_len*U2_len)
        return sim_U1U2_cosine
    elif computeWay == "Jacard":
        #交集
        tempIntersect = 0
        for m,n in zip(i1Arr,i2Arr):
            if m!=0 and n!=0 and m==n:
                tempIntersect +=1
        # 并集
        tempUnion = len(gradedI1)+len(gradedI2)-len(coI1)
        sim_Jacard = tempIntersect/tempUnion
        return sim_Jacard
    elif computeWay == "Pearson":
        I1_len_J = math.sqrt(sum([(i-I1_yiba)*(i-I1_yiba) for i in coI1]))
        I2_len_J = math.sqrt(sum([(j-I2_yiba)*(j-I2_yiba) for j in coI2]))
        I1I2_J = sum([(i-I1_yiba)*(j-I2_yiba) for i,j in zip(coI1,coI2)])
        sim_I1I2_pearson = I1I2_J/(I1_len_J*I2_len_J)
        return sim_I1I2_pearson


def main():
    user_itemArr = buliduser_itemMatrix()


if __name__ == '__main__':
    main()

