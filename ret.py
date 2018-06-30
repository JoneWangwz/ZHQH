 # -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 22:02:45 2018

@author: 王钊
"""
'''
生成ret表和result表

随便选取一个表的日期date，例如testing2Model\A.csv
TrainingResult,表示按日期出来的每天结果
testingStand,测试数据的标准化

'''

import pandas as pd
import numpy as np


def combinationTable(date,testingStand,TrainingResult):
    df =pd.read_csv(date,encoding='gbk')
    trainDay=[]
    tradingDay=[]
    mark2Market=[]
    variety=[]
    sign=[]
    tradingPrice=[]
    nextTradingPrice=[]
    ret=[]
    result={}
    numRet=[]
    net=[]
    NET={}
    date=[]
    for i in range(1,df.shape[0]-1):
        
        dff=pd.read_csv(TrainingResult+"\%s.csv"%(df.loc[i,'日期']),encoding='gbk')
        num=0
        for j in range(dff.shape[0]):
            #num=0
            testdf=pd.read_csv(testingStand+"\%s.csv"%(dff.loc[j,'合约']),encoding='gbk')
            trainDay.append(df.loc[i-1,'日期'])
            tradingDay.append(df.loc[i,'日期'])
            mark2Market.append(df.loc[i+1,'日期'])
            variety.append(dff.loc[j,'合约'])
            if dff.loc[j,'方向']==0:
                dff.loc[j,'方向']=-1
            sign.append(dff.loc[j,'方向'])
            tradingPrice.append(testdf.loc[i,'开盘价1'])
            nextTradingPrice.append(testdf.loc[i,'下一开盘价'])
            num+=(testdf.loc[i,'下一开盘价']-testdf.loc[i,'开盘价1'])/testdf.loc[i,'开盘价1']*dff.loc[j,'方向']
            ret.append((testdf.loc[i,'下一开盘价']-testdf.loc[i,'开盘价1'])/testdf.loc[i,'开盘价1']*dff.loc[j,'方向'])
        numRet.append(num)
        print('numRet',len(numRet))
        print('num',numRet[i-1])
        print('i',i)
        print('df.loc[i,"日期"]',df.loc[i,'日期'])
        if df.loc[i,'日期']==20180103:
            nn=1
            net.append(nn)
        else:
            net.append(net[i-2]*(1+numRet[i-1]/10))
        date.append(df.loc[i,'日期'])
    NET={'日期':date,'ret':numRet,'net':net}    
    result={'训练日':trainDay,'交易日':tradingDay,'盯市日':mark2Market,'品种':variety,'多空标志':sign,
            '开仓价格':tradingPrice,'盯市价格':nextTradingPrice,'收益率':ret}
    re=pd.DataFrame(data=result,columns=['训练日','交易日','盯市日','品种','多空标志','开仓价格','盯市价格',
                                         '收益率'])
    NET=pd.DataFrame(data=NET,columns=['日期','ret','net'])
    re.to_csv(TrainingResult+'/result.csv',encoding='gbk',index=False)
    NET.to_csv(TrainingResult+'/NET.csv',encoding='gbk',index=False)