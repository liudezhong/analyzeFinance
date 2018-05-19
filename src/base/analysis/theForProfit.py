# -*- coding: UTF-8 -*-
import src.base.analysis.statisticsFunc as doStatisticsFunc
import src.base.constans.CalcIndex as calcIndexEnum
import src.base.constans.CompetitiveEdge as comptiEnum

'''
分析盈利性，通过百分率利润表来观察:
    1、营业收入
    2、销售费用
    3、毛利率
    4、财务费用
    5、管理费用
    6、其他利润
    7、营业毛利率
'''
def calPercentageProfitStatement(code):
    sliceList = [calcIndexEnum.CalcIndex.OperationRevenue.value,
                 calcIndexEnum.CalcIndex.SelledExpense.value,
                 calcIndexEnum.CalcIndex.GrossProfitRate.value,
                 calcIndexEnum.CalcIndex.FinanceExpense.value,
                 calcIndexEnum.CalcIndex.AdministrationExpense.value,
                 calcIndexEnum.CalcIndex.OtherOperatingProfit.value,
                 calcIndexEnum.CalcIndex.OperatingMargin.value,
                 ]
    doStatisticsFunc.statisticsMultiBaseFunc(code, sliceList, comptiEnum.CompetitiveEdge.TheForProfit.value)

if __name__ == '__main__':
    calPercentageProfitStatement('002024')
