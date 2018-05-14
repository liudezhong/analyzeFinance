# -*- coding: UTF-8 -*-
import src.base.commons.commonUtils as commUtils
import pandas as pd
import matplotlib.pyplot as plt

'''
分析竞争优势:
    1、自由现金流
    2、毛利率
    3、净资产收益率
    4、资产收益率 = 净收益/公司全部资产
'''
def competitiveAdvantage():
    pass


# 评估历史盈利能力
def historicalProfitability(export, type, code):
    # 展示自由现金流 1、按照报告周期 2、季度 3、年
    analyzeTableFileName = commUtils.getAnalysisFilePath(export, type, code) # 'analysis', 'report', '002024'
    df = pd.read_excel(analyzeTableFileName, sheet_name='analysis')
    table = df.iloc[25:26]
    print(table)
    table.plot(kind='bar')
    plt.show()

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