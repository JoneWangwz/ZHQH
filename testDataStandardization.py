# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 09:47:10 2018

@author: 王钊
"""
'''
speciesList品种列表,variety.txt
testingData 测试数据来源
testingStand 存放地址
testDataStand('variety.txt','testingData','testingStand')
'''

from scipy.stats import norm
import pandas as pd
import numpy as np
def testDataStand(speciesList,testingData,testingStand):
    
    dff = pd.read_csv(speciesList,encoding='gbk',header=None)
    dff.sort_index(inplace=True)

    for i in range(len(dff.loc[:,0])):
    #dff=np.array(dff)
    #print(dff[i])
        df=pd.read_csv(testingData+'/%s.csv'%dff.iloc[i,0],encoding='gbk')
        df.sort_index(inplace=True)
    #df=df.replace('None',0)
    #print(df)
        def norm_NM(Name):
            mid = df.loc[:,Name].median()
        #mid = np.median(df.loc[:,Name])
            qua = df.loc[:,Name].quantile(.75) - df.loc[:,Name].quantile(.25)
            norm_1 = (1/2) * ((df.loc[:,Name]-mid) / qua)
            df[Name] = (100 * norm.cdf(norm_1) - 50)
    
        ma_list = [5, 10, 20, 30, 40, 60]
        def MA(ma_list,Name):
    
# 计算简单算术移动平均线MA - 注意：stock_data['close']为股票每天的收盘价
            for ma in ma_list:
                df['MA_' + str(ma)] = pd.rolling_mean(df[Name], ma)
        
                mid = df.loc[:,'MA_' + str(ma)].median()
            #mid = np.median(df.loc[:,Name])
                qua = df.loc[:,'MA_' + str(ma)].quantile(.75) - df.loc[:,'MA_' + str(ma)].quantile(.25)
                norm_1 = (1/2) * ((df.loc[:,'MA_' + str(ma)]-mid) / qua)
                df['MA_' + str(ma)] = (100 * norm.cdf(norm_1) - 50)
            
        def changeOfInventory(Name1):
            df['持仓量1']=df.loc[:,Name1].shift(1)
            df['持仓量变化']=df.loc[:,Name1]-df.loc[:,'持仓量1']
    
    #资金变动=持仓量*今日收盘价
        def movementOfFunds(Name1,Name2):
            df['资金变动']=df.loc[:,Name1]*df.loc[:,Name2]

    #收盘涨跌幅度
        def upAndDownClose(Name1,Name2):
            df['涨跌幅(收盘价)']=(df.loc[:,Name1]/df.loc[:,Name2])
        #分类（0或1）

    #涨跌幅(结算价)    
        def settlementPriceFluctuation(Name1,Name2):
            df['涨跌幅(结算价)']=(df.loc[:,Name1]/df.loc[:,Name2])
        
        
        
        def classify(Name1,Name2):
            df['分类']=df.loc[:,Name1]-df.loc[:,Name2]
            for i in range(len(df['分类'])):
                if df.loc[i,'分类']>0:
                    df.loc[i,'分类']=1
                else:
                    df.loc[i,'分类']=-1
                
        def contributionPrice(Name1,Name2):
            #df['价格变动贡献度']=(df.loc[:,Name1]/df.loc[:,Name2])*1000
            df['价格变动贡献度']=(df.loc[:,Name1]/df.loc[:,Name2])
        def max_min(Name1):
    
            N_max = df.loc[:,Name1].max()
            N_min = df.loc[:,Name1].min()
            df[Name1] = (df.loc[:,Name1] - N_min) / (N_max - N_min)
        
        
        def std_mean(Name2):
            N_std = df.loc[:,Name2].std()#np.mean(df.loc[:,Name2], axis=0)#  df.loc[:,Name2].std()
            N_mean = df.loc[:,Name2].mean()#np.mean(df.loc[:,Name2], axis=0)  #df.loc[:,Name2].mean()
            df[Name2] = (N_std - N_mean) / N_std
        df['收盘价1']=df.loc[:,'收盘价'] 
        df['开盘价1']=df.loc[:,'开盘价']
        df['下一开盘价']=df.loc[:,'开盘价'].shift(-1)
        changeOfInventory('持仓量')
        upAndDownClose('涨跌(收盘价)','前收盘')
        contributionPrice('涨跌(收盘价)','收盘价')
        movementOfFunds('持仓量变化','收盘价')
        settlementPriceFluctuation('涨跌(结算价)','前结算价')
        norm_NM("开盘价")
        norm_NM("最高价")
        norm_NM("最低价")
        norm_NM("收盘价")
        norm_NM("前收盘")
        norm_NM("前结算价")
        norm_NM("结算价")
        
        MA(ma_list,'收盘价')
        norm_NM('涨跌幅(结算价)')
        norm_NM('涨跌幅(收盘价)')
        norm_NM('持仓量变化')
        norm_NM('资金变动')
        norm_NM('价格变动贡献度')
        classify('收盘价','前收盘')
    
        df = df.loc[:,['合约','日期','前收盘','下一开盘价','开盘价','开盘价1','最高价','最低价','收盘价','收盘价1','成交量','成交额','成交笔数','涨跌(收盘价)',
                       '涨跌幅(收盘价)','振幅(收盘价)','均价','持仓量','持仓量变化','前结算价','结算价','涨跌(结算价)','涨跌幅(结算价)',
                       '最近交易日期','市场最近交易日','MA_5','MA_10','MA_20','MA_30','MA_40','MA_60','持仓量变化','资金变动','价格变动贡献度','分类']]
        df=df.fillna(0)
        df.to_csv(testingStand+'/%s.csv'%dff.iloc[i,0],encoding='gbk',index=False)