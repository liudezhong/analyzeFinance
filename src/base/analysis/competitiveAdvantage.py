# -*- coding: UTF-8 -*-
import src.base.commons.commonUtils as commUtils
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
分析竞争优势:
    1、自由现金流
    2、净利润
    3、净资产收益率
    4、资产收益率 = 净收益/公司全部资产
'''
def competitiveAdvantage():
    pass


# 评估历史盈利能力
def historicalProfitability(export, type, code):
    # 展示自由现金流 1、按照报告周期 2、季度 3、年
    analyzeTableFileName = commUtils.getAnalysisFilePath(export, type, code) # 'analysis', 'report', '002024'
    df = pd.read_excel(analyzeTableFileName, sheet_name='analysis', header = 0)
    print(df.values[25][0])
    print(len(df.values[25][1:]))
    df1 = pd.DataFrame({df.values[24][0]: df.values[24][1:]})
    df2 = pd.DataFrame({df.values[25][0]: df.values[25][1:]})
    df3 = pd.DataFrame({df.values[26][0]: df.values[26][1:]})
    df4 = pd.DataFrame({df.values[4][0]: df.values[4][1:]})
    fig1 = plt.figure(figsize = (10, 8))
    ax1 = fig1.add_subplot(2, 2, 1)
    ax2 = fig1.add_subplot(2, 2, 2)
    ax3 = fig1.add_subplot(2, 2, 3)
    ax4 = fig1.add_subplot(2, 2, 4)
    ax1.set_xticks(np.arange(17))
    # ax1.set_xticklabels([df.values[24][0]])
    ax1.plot(df1, color='green', linestyle='dashed', marker='o',
                 markerfacecolor='blue', markersize=5, label='line 1')
    ax2.plot(df2, color='green', linestyle='dashed', marker='o',
                 markerfacecolor='red', markersize=5, label='line 1')
    ax3.plot(df3, color='green', linestyle='dashed', marker='o',
                 markerfacecolor='green', markersize=5, label='line 1')
    ax4.plot(df4, color='green', linestyle='dashed', marker='o',
                 markerfacecolor='yellow', markersize=5, label='line 1')
    # df1.plot(kind = 'bar')
    plt.show()
    print(df1)
    # print(df.columns[1:])
    # table.plot(kind='bar')
    # plt.show()

# 评估利润来源
def sourceOfProfits():
    pass

# 评估竞争优势周期
def evaluateCompetitiveAdvantageCycle():
    pass

# 分析行业结构
def analysisIndustryStructure():
    pass


if __name__ == '__main__':
    historicalProfitability('analysis', 'year', '002024')
    # historicalProfitability('analysis', 'report', '002024')