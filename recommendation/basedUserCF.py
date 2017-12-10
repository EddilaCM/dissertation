# -*- coding:utf-8 -*-
# __author__ = 'cm'
import pandas as pd
import numpy as np
import math


class basedUserCF:
    def __init__(self,trainfile,testFile,recomendPeoplefile,simiThreshold=0.5,topN=10):
        self.testSet =self.readFile(trainfile)
        self.trainningSet =self.readFile(testFile)
        self.recoPeople =self.readFile(recomendPeoplefile)
        self.simiThreshold = simiThreshold
        self.topN = topN

    # 读文件  返回数据
    def readFile(self,fileName):
        fileType = fileName.split('.')[1]
        print fileType
        if fileType == 'csv':
            return pd.read_csv(fileName)
        elif fileType == 'json':
            return pd.read_json(fileName)
        else:
            print("Error: can't read <"+fileType+"> file")

    # 计算用户浏览记录相似度
    def computeSimilary(self,u1,u2,computeWay):
        #行计算，返回两个user的相似度
        user_itemArr = self.trainningSet
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
        if computeWay =="coOccur":
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

    def TopNSimiPeople(self):
        allRecoPeople = self.recoPeople['user']
        trainPeople = self.trainningSet.index
        list = []
        sort = []
        for i,u1 in enumerate(allRecoPeople):
            restperson = trainPeople.remove(u1)
            for u2 in restperson:
                simi = self.computeSimilary(u1,u2,'coOccur')
                if simi>self.simiThreshold:
                    list[u1].append({u2:simi})
            sort[u1] = sorted(list[u1].items,key=lambda e:e(1),reverse=True)
        pass

    def estimateReco(self):
        pass