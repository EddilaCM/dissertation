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


def userSimilarity(user_itemArr,u1,u2,computeWay):
    #行计算，返回两个user的相似度
    user1 = user_itemArr[u1]
    user2 = user_itemArr[u2]
    # 均值
    U1_yiba = sum(user1)/len(user1)
    U2_yiba = sum(user2)/len(user2)
    # 共同评分的项-各自的平均值，再进行余弦计算
    coU1 = []
    coU2 = []
    for i1,i2 in zip(user1,user2):
        if i1!=0 and i2!=0:
            coU1.append(i1)
            coU2.append(i2)
    # 各自评过分的项
    gradedU1 = []; gradedU2 = []
    for U1,U2 in zip(user1,user2):
        if U1 !=0:
            gradedU1.append(U1)
        if U2 != 0:
            gradedU2.append(U2)
    if computeWay =="gongxian":
        tempCoOccurenceNum = 0;
        for U1,U2 in zip(user1,user2):
            if U1!=0 and U2!=0:
                tempCoOccurenceNum +=1
        coOccurentRate = tempCoOccurenceNum/len(user1)
        return coOccurentRate
    elif computeWay == "cosine":
        U1_len = math.sqrt(sum([i*i for i in user1]))
        U2_len = math.sqrt(sum([j*j for j in user2]))
        U1_U2 = sum([i*j for i,j in zip(user1,user2)])
        sim_U1U2_cosine = U1_U2/(U1_len*U2_len)
        return sim_U1U2_cosine
    elif computeWay == "adjustedcosine":
        #与pearson的区别：修正的cosine 分母是user ij 各自评过分的项;pearson 的分母是共同评分的项，分子都是共同评分的项
        U1_len = math.sqrt(sum([(i-U1_yiba)*(i-U1_yiba) for i in gradedU1]))
        U2_len = math.sqrt(sum([(j-U2_yiba)*(j-U2_yiba) for j in gradedU2]))
        U1_U2 = sum([(i-U1_yiba)*(j-U2_yiba) for i,j in zip(coU1,coU2)])
        sim_U1U2_cosine = U1_U2/(U1_len*U2_len)
        return sim_U1U2_cosine
    elif computeWay == "Jcard":
        #交集
        tempIntersect = 0
        for m,n in zip(user1,user2):
            if m!=0 and n!=0 and m==n:
                tempIntersect +=1
        # 并集
        tempUnion = len(gradedU1)+len(gradedU2)-len(coU1)
        sim_Jacard = tempIntersect/tempUnion
        return sim_Jacard
    elif computeWay == "Pearson":
        U1_len_J = math.sqrt(sum([(i-U1_yiba)*(i-U1_yiba) for i in coU1]))
        U2_len_J = math.sqrt(sum([(j-U2_yiba)*(j-U2_yiba) for j in coU2]))
        U1U2_J = sum([(i-U1_yiba)*(j-U2_yiba) for i,j in zip(coU1,coU2)])
        sim_U1U2_pearson = U1U2_J/(U1_len_J*U2_len_J)
        return  sim_U1U2_pearson


def main():
    user_itemArr = buliduser_itemMatrix()


if __name__ == '__main__':
    main()

