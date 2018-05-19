# -*- coding: UTF-8 -*-
import src.base.analysis.statisticsFunc as doStatisticsFunc
import src.base.constans.CalcIndex as calcIndexEnum
import src.base.constans.CompetitiveEdge as comptiEnum

'''
评估财务健康状况
    1、负债权益比率（产权比率）
    2、流动比率
    3、速动比率
    4、保守速动比率
'''
def calfinancialHealth(code):
    sliceList = [calcIndexEnum.CalcIndex.DebtEquityRatio.value,
                 calcIndexEnum.CalcIndex.CurrentRatio.value,
                 calcIndexEnum.CalcIndex.QuickRatio.value,
                 calcIndexEnum.CalcIndex.ConserQuickRatio.value
                 ]
    doStatisticsFunc.statisticsSingleBaseFunc(code, sliceList, comptiEnum.CompetitiveEdge.FinancialHealth.value)

if __name__ == '__main__':
    calfinancialHealth('002024')

