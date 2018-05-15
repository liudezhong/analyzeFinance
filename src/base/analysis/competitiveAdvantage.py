# -*- coding: UTF-8 -*-
import src.base.commons.commonUtils as commUtils
import src.base.constans.CalcIndex as calcIndexEnum
import pandas as pd

from matplotlib.font_manager import _rebuild

_rebuild()  # reload一下

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
    analyzeTableFileName = commUtils.getAnalysisFilePath(export, type, code)  # 'analysis', 'report', '002024'
    df = pd.read_excel(analyzeTableFileName, sheet_name='analysis', header=0)
    enumList = commUtils.historicalProfitabilityEnumIndex([calcIndexEnum.CalcIndex.FreeCashFlow.value,
                                                           calcIndexEnum.CalcIndex.GrossProfitRate.value,
                                                           calcIndexEnum.CalcIndex.ReturnOnEquity.value,
                                                           calcIndexEnum.CalcIndex.ReturnOnAssets.value])
    print(enumList)
    commUtils.showPlot(df, enumList, export, type, code, 'historicalProfitability')


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
    # analyzeTableFileName = commUtils.getAnalysisFilePath('analysis', 'year', '002024')  # 'analysis', 'report', '002024'
    # df = pd.read_excel(analyzeTableFileName, sheet_name='analysis', header=0)
    historicalProfitability('analysis', 'simple', '002024')
    # historicalProfitability('analysis', 'report', '002024')
    # showPlot(df, [24, 25, 26, 27])
