# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 22:03:51 2018
@author: 王钊
"""

import pandas as pd
import os
from sklearn.model_selection import train_test_split
import csv
from sklearn.linear_model import LogisticRegression
import numpy as np

'''
dateTable,随便去一个表中的时间testingStand/A.csv
date,单日的计算,例如20180101
dateBegin,计算一段时间的结果的开始时间
dateEnd，计算一段时间的结果的结束时间
trendSort,表示方向的文件的品种文件,TrainingResult/sort
training2Model,训练数据的存放样本的文件夹
testing2Model,测试数据的存放样本的文件夹
varietyValue,品种价值的文件，'stock.csv'
oneResult,单日计算结果存放的文件路径，TrainingResult
manyDaysResult，多日计算结果存放的文件路径，TrainingResult
'''


def filtrate(dateTable, date, dateBegin, dateEnd, trendSort, training2Model, testing2Model, varietyValue,
             oneResult):
    # fd=pd.read_csv(variety+'.txt',encoding='gbk')
    df = pd.read_csv(dateTable, encoding='gbk')
    # dd=pd.read_csv('testingStand/A.csv',encoding='gbk')
    if (float(date) > 20180101):
        if (float(date) <= df.loc[df.shape[0] - 1, '日期']):
            '''
            if os.path.exists('TrainingResult/%s.csv'%(date)):


                #ss=pd.read_csv(testCSV, encoding='gbk')
                #print('ss.shape[0]',ss.shape[0])
                for mk in range(fd.shape[0]):
                    dd=pd.read_csv('testingStand/%s'%(fd.iloc[mk,0]),encoding='gbk')
                    for xx in range(dd.shape[0]):
                        if  dd.loc[xx,'日期']==date:
            '''
            # ss=pd.read_csv(testCSV, encoding='gbk')
            # print('ss.shape[0]',ss.shape[0])
            for xx in range(df.shape[0]):
                if str(df.loc[xx, '日期']) == str(date):

                    conNum = []
                    contract = []
                    closingPrice = []
                    variety = []
                    date = []
                    predic = []
                    trend = []
                    value = []
                    result = {}
                    aLL = [0, 1]
                    for al in aLL:
                        num = 0
                        dff = pd.read_csv(trendSort + '/sort%s.csv' % (str(al)), parse_dates=True, encoding='gbk')
                        dff.sort_index(inplace=True)
                        for f in range(len(dff.iloc[1:, 0])):
                            vv = pd.read_csv(training2Model + '/%s.csv' % (dff.iloc[f, 0]), encoding='gbk',
                                             parse_dates=True)
                            dd = pd.read_csv("testing2Model/%s.csv" %( dff.iloc[f, 0]), encoding='gbk')
                            # print('dd.shape[0]',dd.shape[0])
                            for cc in range(dd.shape[0]):
                                if dd.loc[cc, '日期'] == df.loc[xx, '日期']:
                                    with open(training2Model + '/%s.csv' % dff.iloc[f, 0]) as csvfile:
                                        readCSV = csv.reader(csvfile, delimiter=',')
                                        next(readCSV)
                                        X = []
                                        y = []
                                        for row in readCSV:
                                            X.append(np.array(row[3:len(row[:]) - 1]))
                                            y.append(float(row[-1]))
                                    X.append(dd.iloc[cc, 3:-1])
                                    y.append(float(dd.iloc[cc, -1]))
                                    X = np.array(X)
                                    print('X.shape[1]', X.shape[1])
                                    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                                                        train_size=(X.shape[0] - 1),
                                                                                        shuffle=False)
                                    X_train = np.array(X_train)
                                    y_train = np.array(y_train)
                                    X_test = np.array(X_test)
                                    y_test = np.array(y_test)
                                    x_test = []
                                    x_test = np.array(x_test)
                                    print("\n")
                                    print("开始训练品类%s" % dff.iloc[f, 0])
                                    ml = []
                                    print("dff.loc[f,'combination']", dff.loc[f, 'combination'])
                                    for i in dff.loc[f, 'combination']:
                                        if i == '(':
                                            (dff.loc[f, 'combination'])
                                        elif i == ')':
                                            (dff.loc[f, 'combination'])
                                        elif i == ',':
                                            (dff.loc[f, 'combination'])
                                        elif i == ' ':
                                            (dff.loc[f, 'combination'])
                                        else:
                                            ml.append(int(i))

                                    print('ml', len(ml))
                                    x_train = np.zeros(shape=(X_train.shape[0], len(ml)))
                                    # 初始化测试集
                                    x_test = np.zeros(shape=(X_test.shape[0], len(ml)))
                                    for m in range(len(ml)):
                                        print('m', m)
                                    ll = ml[m]
                                    x_train[:, m] = X_train[:, ll]
                                    x_test[:, m] = X_test[:, ll]
                                    clf = LogisticRegression().fit(x_train, y_train)
                                    print('x_test', x_test.shape)
                                    a = clf.predict(x_test)
                                    if a == dff.loc[f, 'trend']:
                                        shou = pd.read_csv(varietyValue, parse_dates=True, encoding='gbk')
                                        print('shou', shou.shape[0])
                                        for s in range(shou.shape[0]):
                                            if shou.loc[s, '合约代码'] == dff.loc[f, 'category'].lower():

                                                print("shou.loc[s,'合约乘数']", shou.loc[s, '合约乘数'])
                                                com = shou.loc[s, '合约乘数']
                                                if str(com).isdigit():

                                                    contract.append(shou.loc[s, '合约乘数'])
                                                    value.append(shou.loc[s, '合约乘数'] * dd.loc[cc, '收盘价1'])
                                                    conNum.append(int(3000000 / (
                                                    shou.loc[s, '合约乘数'] * vv.loc[vv.shape[0] - 1, '收盘价1'])))
                                                else:
                                                    contract.append(0)
                                                    value.append(0)
                                                    conNum.append(0)
                                        predic.append(a)
                                        trend.append(dff.loc[f, 'trend'])
                                        date.append(dd.loc[cc, '日期'])
                                        variety.append(dff.iloc[f, 0])
                                        closingPrice.append(dd.loc[cc, '收盘价1'])

                                        num += 1

                                    if num >= 5:
                                        break
                                if num >= 5:
                                    break
                            vv = vv.drop([vv.shape[0] - 1])
                    print('variety', len(variety))
                    print('date', len(date))
                    print('trend', len(trend))
                    print('predic', len(predic))
                    print('closingPrice', len(closingPrice))
                    print('contract', len(contract))
                    print('value', len(value))
                    print('conNum', len(conNum))
                    result = {'合约': variety, '日期': date, '方向': trend, '预测': predic, '收盘价1': closingPrice,
                              '合约乘数': contract, '价值': value, '数量': conNum}
                    re = pd.DataFrame(data=result, columns=['合约', '日期', '方向', '预测', '收盘价1', '合约乘数', '价值', '数量'])
                    re.to_csv(oneResult + '/1%s.csv' % (str(date[0])), encoding='gbk', index=False)
                    print(date)

                    # dd=pd.read_csv('TrainingResult/%s.csv'%(date),encoding='gbk')
                    # dd.to_csv('%s.txt'%(date),encoding='gbk',index=False)
        else:
            print("输入日期可能不为交易日")
    else:
        print("输入日期开始日期必须是2018年以后")
    # sumBegin=0
    # sumEnd=0
    if dateBegin > 20180101:
        if dateBegin < dateEnd:

            if dateBegin > 20180101:
                if dateBegin <= df.loc[df.shape[0] - 2, '日期']:
                    if dateEnd > 20180101:
                        if dateEnd < df.loc[df.shape[0] - 1, '日期']:
                            '''
                            for i in range(df.shape[0]):
                                if df.loc[i,'日期']==dateBegin:
                                    sumBegin=i
                                if df.loc[i,'日期']==dateEnd:
                                    sumEnd=i
                            '''

                            conNum = []
                            contract = []
                            closingPrice = []
                            variety = []
                            date = []
                            predic = []
                            trend = []
                            value = []
                            result = {}
                            for xx in range(df.shape[0]):
                                if df.loc[xx, '日期'] >= dateBegin:
                                    if df.loc[xx, '日期'] <= dateEnd:

                                        aLL = [0, 1]
                                        for al in aLL:
                                            nu = 0
                                            dff = pd.read_csv(trendSort + '/sort%s.csv' % (str(al)), parse_dates=True,
                                                              encoding='gbk')
                                            dff.sort_index(inplace=True)
                                            for f in range(len(dff.iloc[1:, 0])):
                                                vv = pd.read_csv(training2Model + '/%s.csv' % dff.iloc[f, 0],
                                                                 encoding='gbk', parse_dates=True)
                                                dd = pd.read_csv('testing2Model/%s.csv' % dff.iloc[f, 0],
                                                                 encoding='gbk', parse_dates=True)
                                                # print('dd.shape[0]',dd.shape[0])
                                                for cc in range(dd.shape[0]):
                                                    if dd.loc[cc, '日期'] == df.loc[xx, '日期']:
                                                        # if dd.loc[cc,'日期']<=float(dateEnd):
                                                        # num=0
                                                        with open(training2Model + '/%s.csv' % dff.iloc[
                                                            f, 0]) as csvfile:
                                                            readCSV = csv.reader(csvfile, delimiter=',')
                                                            next(readCSV)
                                                            X = []
                                                            y = []
                                                            for row in readCSV:
                                                                X.append(np.array(row[3:len(row[:]) - 1]))
                                                                y.append(float(row[-1]))
                                                        X.append(dd.iloc[cc, 3:-1])
                                                        y.append(float(dd.iloc[cc, -1]))
                                                        X = np.array(X)
                                                        print('X.shape[1]', X.shape[1])
                                                        X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                                                                            train_size=(
                                                                                                            X.shape[
                                                                                                                0] - 1),
                                                                                                            shuffle=False)
                                                        X_train = np.array(X_train)
                                                        y_train = np.array(y_train)
                                                        X_test = np.array(X_test)
                                                        y_test = np.array(y_test)
                                                        x_test = []
                                                        x_test = np.array(x_test)
                                                        print("\n")
                                                        print("开始训练品类%s" % dff.iloc[f, 0])
                                                        ml = []
                                                        print("dff.loc[f,'combination']", dff.loc[f, 'combination'])
                                                        for i in dff.loc[f, 'combination']:
                                                            if i == '(':
                                                                (dff.loc[f, 'combination'])
                                                            elif i == ')':
                                                                (dff.loc[f, 'combination'])
                                                            elif i == ',':
                                                                (dff.loc[f, 'combination'])
                                                            elif i == ' ':
                                                                (dff.loc[f, 'combination'])
                                                            else:
                                                                ml.append(int(i))

                                                        print('ml', len(ml))
                                                        x_train = np.zeros(shape=(X_train.shape[0], len(ml)))
                                                        # 初始化测试集
                                                        x_test = np.zeros(shape=(X_test.shape[0], len(ml)))
                                                        for m in range(len(ml)):
                                                            print('m', m)
                                                        ll = ml[m]
                                                        x_train[:, m] = X_train[:, ll]
                                                        x_test[:, m] = X_test[:, ll]
                                                        clf = LogisticRegression().fit(x_train, y_train)
                                                        print('x_test', x_test.shape)
                                                        a = clf.predict(x_test)
                                                        if a == dff.loc[f, 'trend']:
                                                            shou = pd.read_csv(varietyValue, parse_dates=True,
                                                                               encoding='gbk')
                                                            print('shou', shou.shape[0])
                                                            for s in range(shou.shape[0]):
                                                                if shou.loc[s, '合约代码'] == dff.loc[
                                                                    f, 'category'].lower():

                                                                    print("shou.loc[s,'合约乘数']", shou.loc[s, '合约乘数'])
                                                                    com = shou.loc[s, '合约乘数']
                                                                    if str(com).isdigit():

                                                                        contract.append(shou.loc[s, '合约乘数'])
                                                                        value.append(
                                                                            shou.loc[s, '合约乘数'] * dd.loc[cc, '收盘价1'])
                                                                        conNum.append(int(3000000 / (
                                                                        shou.loc[s, '合约乘数'] * vv.loc[
                                                                            vv.shape[0] - 1, '收盘价1'])))
                                                                    else:
                                                                        contract.append(0)
                                                                        value.append(0)
                                                                        conNum.append(0)
                                                            predic.append(a)
                                                            trend.append(dff.loc[f, 'trend'])
                                                            date.append(dd.loc[cc, '日期'])
                                                            variety.append(dff.iloc[f, 0])
                                                            closingPrice.append(dd.loc[cc, '收盘价1'])

                                                            nu += 1
                                                        if nu >= 5:
                                                            break
                                                            # if nu>=5:
                                                            #   break
                                                    if nu >= 5:
                                                        break
                                                vv = vv.drop([vv.shape[0] - 1])
                                                # if num>=5:
                                                # break
                                        print('variety', len(variety))
                                        print('date', len(date))
                                        print('trend', len(trend))
                                        print('predic', len(predic))
                                        print('closingPrice', len(closingPrice))
                                        print('contract', len(contract))
                                        print('value', len(value))
                                        print('conNum', len(conNum))
                                        result = {'合约': variety, '日期': date, '方向': trend, '预测': predic,
                                                  '收盘价1': closingPrice,
                                                  '合约乘数': contract, '价值': value, '数量': conNum}
                                        re = pd.DataFrame(data=result,
                                                          columns=['合约', '日期', '方向', '预测', '收盘价1', '合约乘数', '价值', '数量'])
                                        re = re.sort_values(by=['日期', '方向'])
                                        re.to_csv(oneResult + '/%sAnd%s.csv' % (str(dateBegin), str(dateEnd)),
                                                  encoding='gbk', index=False)




                                        # for j in range(sumBegin,sumEnd+1):

                        else:
                            print('结束日期必须是存在于当前列表中')
                else:
                    print("结束日期必须是存在于当前列表中")
            else:
                print("输入日期必须是2018年以后1")
    else:
        print('开始日期必须是2018年以后1')

if __name__=='__main__':

    date = input("请输入一天的预测:")
    #date = float(date)
    # print(date)
    yes = input("请输入是否需要训练时间段 yes/no：")
    # no=input("不与要训练输入no：")
    if yes == 'yes':

        dateBegin = input("请输入开始的时间：")
        dateEnd = input("请输入结束的时间：")
        dateBegin = float(dateBegin)
        dateEnd = float(dateEnd)
    elif yes == 'no':
        dateBegin = 0
        dateEnd = 0
    else:
        print("输入错误")

    '''
    dateBegin = 0
    dateEnd = 0
    date=20180402
    '''
    filtrate('testingStand/A.csv', date, dateBegin, dateEnd, 'TrainingResult/sort', 'training2Model',' testing2Model', 'stock.csv','TrainingResult')