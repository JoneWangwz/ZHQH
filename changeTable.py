# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 09:47:42 2018

@author: 王钊
"""
'''
testCSV,任意测试文件，主要提取日期 例如testing2Model\A.csv
trainResult,结果
'''
import pandas as pd

def change(testCSV,TrainingResult):
    df =pd.read_csv(testCSV,encoding='gbk')
    
    for i in range(df.shape[0]-1):
        change=[]
        contract=[]
        date=[]
        result={}
        dff=pd.read_csv(TrainingResult+"\%s.csv"%(df.loc[i,'日期']),encoding='gbk')
        #dff=pd.read_csv('TrainingResult\%s.csv'%(df.[i,'日期']),encoding='gbk')
        cdf=pd.read_csv(TrainingResult+'\%s.csv'%(df.loc[i+1,'日期']),encoding='gbk')
        for j in range(dff.shape[0]):
            m=0
            #n=0
            for k in range(cdf.shape[0]):
                print(df.loc[i+1,'日期'])
                print('dff.loc[j,"方向"]',dff.loc[j,'方向'])
                print('cdf.loc[j,"方向"]',cdf.loc[k,'方向'])
                if dff.loc[j,'方向']==cdf.loc[k,'方向']:
                    #m+=1
                    if dff.loc[j,'合约']==cdf.loc[k,'合约']:
                        change.append('不变')
                        contract.append(dff.loc[j,'合约'])
                        date.append(df.loc[i+1,'日期'])
                        #break
                    elif dff.loc[j,'合约']!=cdf.loc[k,'合约']:
                        m+=1
                    else:
                        print(m)
                    if (m==5):
                        change.append('删除')
                        contract.append(dff.loc[j,'合约'])
                        date.append(df.loc[i+1,'日期'])
        for c in range(cdf.shape[0]):
            n=0
            for u in range(dff.shape[0]):
                
                if cdf.loc[c,'方向']==dff.loc[u,'方向']:
                    
                    if cdf.loc[c,'合约']!=dff.loc[u,'合约']:
                        n+=1
                    if n==5:
                        change.append('新增')
                        contract.append(cdf.loc[c,'合约'])
                        date.append(df.loc[i+1,'日期'])
                        #break
                    
        
        result={'合约':contract,'日期':date,'变化':change}
        re=pd.DataFrame(data=result,columns=['合约','日期','变化'])
        re.to_csv(TrainingResult+'/change%s.csv'%(df.loc[i+1,'日期']),encoding='gbk',index=False)
                        
                        
                    
                    