# -*- coding: UTF-8 -*-
import src.base.analysis.statisticsFunc as doStatisticsFunc
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
    # 评估历史盈利能力
    caHlistoricalProfitability(code)
    # 评估自由现金流的组成
    calCheckFreeCashFlowComposition(code)
    # 评估盈利能力
    calProfitability(code)

# 评估自由现金流的组成
def calCheckFreeCashFlowComposition(code):
    sliceList = [calcIndexEnum.CalcIndex.BusiAmount.value,
                 calcIndexEnum.CalcIndex.BuildFixedAssetsAmount.value,
                 calcIndexEnum.CalcIndex.FreeCashFlow.value,
                 ]
    doStatisticsFunc.statisticsSingleBaseFunc(code, sliceList, comptiEnum.CompetitiveEdge.AnalysisFreeCashFlow.value)

# 评估历史盈利能力
def caHlistoricalProfitability(code):
    sliceList = [calcIndexEnum.CalcIndex.FreeCashFlow.value,
                 calcIndexEnum.CalcIndex.FreeCashFlowDivideSell.value,
                 calcIndexEnum.CalcIndex.GrossProfitRate.value,
                 calcIndexEnum.CalcIndex.ReturnOnEquity.value,
                 calcIndexEnum.CalcIndex.ReturnOnAssets.value
                 ]
    doStatisticsFunc.statisticsMultiBaseFunc(code, sliceList, comptiEnum.CompetitiveEdge.HistoricalProfitability.value)

# 评估盈利能力 营业毛利率、销售净利率、资产周转率、资产收益率、负债权益比率（财务杠杆比率）、净资产收益率
def calProfitability(code):
    sliceList = [calcIndexEnum.CalcIndex.OperatingMargin.value,
                 calcIndexEnum.CalcIndex.NetProfitMarginOnSales.value,
                 calcIndexEnum.CalcIndex.TotalAssetsTurnover.value,
                 calcIndexEnum.CalcIndex.ReturnOnAssets.value,
                 calcIndexEnum.CalcIndex.DebtEquityRatio.value,
                 calcIndexEnum.CalcIndex.ReturnOnEquity.value
                 ]
    doStatisticsFunc.statisticsMultiBaseFunc(code, sliceList, comptiEnum.CompetitiveEdge.Profitability.value)

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
