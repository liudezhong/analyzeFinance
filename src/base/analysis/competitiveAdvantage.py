# -*- coding: UTF-8 -*-
import src.base.commons.commonUtils as commUtils
import src.base.constans.CalcIndex as calcIndexEnum
import src.base.constans.CompetitiveEdge as comptiEnum

'''
分析竞争优势:
    1、自由现金流
    2、毛利率
    3、净资产收益率
    4、资产收益率 = 净收益/公司全部资产
'''

def competitiveAdvantage(code):
    historicalProfitability(code)
    checkFreeCashFlowComposition(code)


def checkFreeCashFlowComposition(code):
    sliceList = [calcIndexEnum.CalcIndex.BusiAmount.value,
                 calcIndexEnum.CalcIndex.BuildFixedAssetsAmount.value,
                 calcIndexEnum.CalcIndex.FreeCashFlow.value,
                 ]
    commUtils.statisticsSingleBaseFunc(code, sliceList, comptiEnum.CompetitiveEdge.AnalysisFreeCashFlow.value)

# 评估历史盈利能力
def historicalProfitability(code):
    sliceList = [calcIndexEnum.CalcIndex.FreeCashFlow.value,
                 calcIndexEnum.CalcIndex.FreeCashFlowDivideSell.value,
                 calcIndexEnum.CalcIndex.GrossProfitRate.value,
                 calcIndexEnum.CalcIndex.ReturnOnEquity.value,
                 calcIndexEnum.CalcIndex.ReturnOnAssets.value
                 ]
    commUtils.statisticsMultiBaseFunc(code, sliceList, comptiEnum.CompetitiveEdge.HistoricalProfitability.value)

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
    competitiveAdvantage('002024')
