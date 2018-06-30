# -*- coding: utf-8 -*-
"""
Created on Wed May 23 20:12:15 2018

@author: 王钊
"""
'''
对测试数据的日期进行变化，2018/01/1变成20180101
'''

import numpy as np
import pandas as pd
from datetime import datetime 

dff = pd.read_csv("variety.txt",encoding='gbk',header=None)
dff.sort_index(inplace=True)

for i in range(dff.shape[0]):
    print(dff.iloc[i,0])
    df=pd.read_csv('test0106/%s.csv'%dff.iloc[i,0], encoding='gbk')
    #df.loc[:,'日期']=df.iloc[:,1]
    
    for m in range(df.shape[0]):
        try:
            
            df.loc[m,'日期'] = datetime.strptime(df.loc[m,'日期'],'%Y/%m/%d').strftime('%Y%m%d')# 根据字符串本身的格式进行转换
        except:
            continue
        #print(df.loc[i,'日期'])
    recover=[]
    
    #print(type(recover))
    error={}
    for k in range(df.shape[0]):
        if float(df.loc[k,'日期']) > 20171231:
            #for j in range(len(df.loc[i,:])):
                
            recover.append(df.loc[k,:])
            df = df.drop([k])
        
        
    list1=['合约','日期','前收盘','开盘价',
                   '最高价','最低价','收盘价','成交量','成交额','成交笔数','涨跌(收盘价)','涨跌幅(收盘价)',
                   '振幅(收盘价)','均价','持仓量','持仓量变化','前结算价','结算价','涨跌(结算价)','涨跌幅(结算价)',
                   '最近交易日期','市场最近交易日']
    list1=np.array(list1)
    recover=np.array(recover)
    #print('re',recover[:,1].shape)
    #print(list1[1])
    #print(df.shape[1])
    for j in range(df.shape[1]):
        if recover.shape[0]>0:
            error[list1[j]]=recover[:,j]
        #error={list1[j]:recover[:,j]}
    #print(error)
           
    err=pd.DataFrame(error)
    #print('err',err.shape)
    #print('df',df.shape)
    #print(dff.iloc[i,0])
    err.to_csv('testingData/%s.csv'%dff.iloc[i,0],encoding='gbk',index=False)
    #df.to_csv('trainingData/%s.csv'%dff.iloc[i,0],encoding='gbk',index=False)