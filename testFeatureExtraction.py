# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 10:55:16 2018

@author: 王钊
"""
'''
variety 品种的位置
testingStand 测试数据的标准化
testing2Model 生成的数据的保存位置
'''

import time
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

def featureExtraction(variety,testingStand,testing2Model):
    
    dff = pd.read_csv(variety+".txt",encoding='gbk',header=None)
    dff.sort_index(inplace=True)

#print(dff)


#print(dff.iloc[11,0])
    for i in range(len(dff.loc[:,0])):
    #dff=np.array(dff)
    #print(dff[i])
        df=pd.read_csv(testingStand+'/%s.csv'%dff.iloc[i,0],encoding='gbk')
        df.sort_index(inplace=True)
    #timeArray = time.strptime(df['日期'], "%Y/%m/%d")
    #df.loc[:,'日期'] = time.strftime("%Y%m%d", timeArray)
    #print(df)
    #df = df.loc[:,['MA_5','MA_10','MA_20','MA_30','MA_40','MA_60','持仓量变化','资金变动','价格变动贡献度','分类']]
        df=df.loc[:,['合约','日期','收盘价1','价格变动贡献度','资金变动','持仓量变化','MA_60','MA_40','MA_30','MA_20','MA_10','MA_5','分类']]
        df.to_csv(testing2Model+'/%s.csv'%dff.iloc[i,0],encoding='gbk',index=False)

if __name__=='__main__':
    featureExtraction('variety', 'testingStand', 'testing2Model')