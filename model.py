# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 16:01:06 2018

@author: 王钊
"""
from __future__ import division
'''
按日期生成每日数据，每天十个，涨跌分别5个
testCSV,任意测试文件，主要提取日期 例如testing2Model\A.csv
trendSize 涨跌文件所在位置 例 TrainingResult/sort
training2Model 训练文件所在位置
testing2Model  测试文件所在位置
TrainingResult 输出结果所在文件
'''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import csv
#from itertools import combinations
#from sklearn.tree import DecisionTreeClassifier
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.ensemble import ExtraTreesClassifier
#from sklearn.ensemble import BaggingClassifier


zero = 0.000000000001

def train_model_function(testCSV,trendSize,training2Model,testing2Model,TrainingResult):
    
    ss=pd.read_csv(testCSV, encoding='gbk')
    print('ss.shape[0]',ss.shape[0])
    for xx in range(ss.shape[0]):
        conNum=[]
        contract=[]
        closingPrice=[]
        variety=[]
        date=[]
        predic=[]
        trend=[]
        value=[]
        result = {}  
        aLL=[0,1]
        for al in aLL:
            num=0
            dff = pd.read_csv(trendSize+'/sort%s.csv'%(str(al)), parse_dates=True,encoding='gbk')
            dff.sort_index(inplace=True)        
            for f in range(len(dff.iloc[1:, 0])):
                vv=pd.read_csv(training2Model+'/%s.csv' % dff.iloc[f, 0], encoding='gbk', parse_dates=True)
                dd=pd.read_csv(testing2Model+'/%s.csv' % dff.iloc[f, 0], encoding='gbk')
                #print('dd.shape[0]',dd.shape[0])
                for cc in range(dd.shape[0]):
                    if dd.loc[cc,'日期']==ss.loc[xx,'日期']:
                        with open(training2Model+'/%s.csv' % dff.iloc[f, 0],encoding='gbk') as csvfile:
                            readCSV = csv.reader(csvfile, delimiter=',')
                            next(readCSV)
                            X = []
                            y = []
                            for row in readCSV:
                                X.append(np.array(row[3:len(row[:]) - 1]))
                                y.append(float(row[-1]))
                        X.append(dd.iloc[cc,3:-1])
                        y.append(float(dd.iloc[cc,-1]))
                        X = np.array(X)
                        print('X.shape[1]',X.shape[1])
                        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=(X.shape[0]-1),shuffle=False)
                        X_train = np.array(X_train)
                        y_train = np.array(y_train)
                        X_test = np.array(X_test)
                        y_test = np.array(y_test)
                        x_test = []
                        x_test = np.array(x_test)              
                        print("\n")
                        print("开始训练品类%s" % dff.iloc[f, 0])            
                        ml=[]
                        print("dff.loc[f,'combination']",dff.loc[f,'combination'])
                        for i in dff.loc[f,'combination']:
                            if i=='(':
                                (dff.loc[f,'combination'])
                            elif i==')':
                                (dff.loc[f,'combination'])
                            elif i==',':
                                (dff.loc[f,'combination'])
                            elif i==' ':
                                (dff.loc[f,'combination'])
                            else: 
                                ml.append(int(i)) 
                
                        print('ml',len(ml))
                        x_train = np.zeros(shape=(X_train.shape[0], len(ml)))
                        # 初始化测试集
                        x_test = np.zeros(shape=(X_test.shape[0], len(ml)))
                        for m in range(len(ml)):
                            
                            print('m',m)
                            ll=ml[m]
                            x_train[:,m]=X_train[:,ll]
                            x_test[:,m]=X_test[:,ll]                            
                        clf = LogisticRegression().fit(x_train, y_train)                       
                        print('x_test',x_test.shape)
                        a = clf.predict(x_test)
                        if a == dff.loc[f,'trend']:
                            shou=pd.read_csv('stock.csv', parse_dates=True,encoding='gbk')
                            print('shou',shou.shape[0])
                            for s in range(shou.shape[0]):
                                if shou.loc[s,'合约代码']==dff.loc[f,'category'].lower():
                                    print("shou.loc[s,'合约乘数']",shou.loc[s,'合约乘数'])
                                    com=shou.loc[s,'合约乘数']
                                    if str(com).isdigit():
                                        
                                        contract.append(shou.loc[s,'合约乘数'])
                                        value.append(shou.loc[s,'合约乘数']*dd.loc[cc,'收盘价1'])
                                        conNum.append(int(3000000/(shou.loc[s,'合约乘数']*vv.loc[vv.shape[0]-1,'收盘价1'])))
                                    else:
                                        contract.append(0)
                                        value.append(0)
                                        conNum.append(0)
                            predic.append(a)
                            trend.append(dff.loc[f,'trend'])
                            date.append(dd.loc[cc,'日期'])
                            variety.append(dff.iloc[f, 0])
                            closingPrice.append(dd.loc[cc,'收盘价1'])
                            
                            num+=1
                                
                        if num>=5:
                            break
                    if num>=5:
                        break
                vv = vv.drop([vv.shape[0]-1])
        print('variety',len(variety))
        print('date',len(date))
        print('trend',len(trend))
        print('predic',len(predic))     
        print('closingPrice',len(closingPrice))
        print('contract',len(contract))
        print('value',len(value)) 
        print('conNum',len(conNum))
        result = {'合约':variety,'日期':date,'方向':trend,'预测':predic,'收盘价1':closingPrice,
                  '合约乘数':contract,'价值':value,'数量':conNum}
        re=pd.DataFrame(data=result,columns=['合约','日期','方向','预测','收盘价1','合约乘数','价值','数量'])        
        re.to_csv(TrainingResult+'/%s.csv'%(ss.loc[xx,'日期']),encoding='gbk',index=False)

if __name__=='__main__':
    train_model_function('testing2Model/A.csv','TrainingResult/sort',
                         'training2Model','testing2Model','TrainingResult')
        
    