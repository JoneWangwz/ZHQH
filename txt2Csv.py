# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 10:32:30 2018

@author: 王钊
"""

import pandas as pd
#import numpy as np

#step 1：text ---> csv

'''
data_source_path:品类文件路径
data_text_path：数据源text文件夹路径
data_csv_path：数据CSV文件夹路径
例如,我调用品种进行转换, txt2csvFunction('variety.txt','Data','toCsv')
'''

def txt2csvFunction():
    dff = pd.read_csv('variety.txt',header=None)
    dff.sort_index(inplace=True)

    #print(dff)

    
    #print(dff.iloc[11,0])
    for i in range(len(dff.loc[:,0])):
        #dff=np.array(dff)
        #print(dff[i])
       #从左到右对列进行命名
       #df=pd.read_csv('testData/%s.txt'%dff.iloc[i,0])
       #df.to_csv('test0106/%s.csv'%dff.iloc[i,0],encoding='gbk',index=False)
       df=pd.read_csv('Data_0622/%s.txt'%dff.iloc[i,0],names=['合约','日期','前收盘','开盘价',
                   '最高价','最低价','收盘价','成交量','成交额','成交笔数','涨跌(收盘价)','涨跌幅(收盘价)',
                   '振幅(收盘价)','均价','持仓量','持仓量变化','前结算价','结算价','涨跌(结算价)','涨跌幅(结算价)',
                   '最近交易日期','市场最近交易日'])
       print(df.shape[1])
       df.sort_index(inplace=True)
       df=df.replace('None',0)
       df=df.fillna(0)
       
       for j in range(df.shape[0]):
           
           if df.loc[j, '开盘价'] == 0:
                # print(df.shape[1])
                
                df = df.drop([j])
       
        #最后把txt文件写入到csv中，文件个格式，例如“c/qihuo/xx.csv”,%s代表字符，就是把%dff.iloc[i,0]赋值给%s。
       df.to_csv('test0106/%s.csv'%dff.iloc[i,0],encoding='gbk',index=False)