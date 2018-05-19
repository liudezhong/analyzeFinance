# -*- coding: UTF-8 -*-
import src.base.analysis.statisticsFunc as doStatisticsFunc
import src.base.constans.CalcIndex as calcIndexEnum
import src.base.constans.CompetitiveEdge as comptiEnum

# 评估成长性 净利润，扣非净利润，净利润同比增长率、扣非净利润同比增长率
def calGrowth(code):
    sliceList = [calcIndexEnum.CalcIndex.RetainedProfits.value,
                 calcIndexEnum.CalcIndex.RetainedProfitsGrowth.value,
                 calcIndexEnum.CalcIndex.TakeNonRetainedProfits.value,
                 calcIndexEnum.CalcIndex.NonNetRetainedProfitsGrowth.value,
                 ]
    doStatisticsFunc.statisticsMultiBaseFunc(code, sliceList, comptiEnum.CompetitiveEdge.Growth.value)

if __name__ == '__main__':
    calGrowth('002024')