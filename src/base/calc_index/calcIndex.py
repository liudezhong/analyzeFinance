# -*- coding: UTF-8 -*-

import src.base.read_data.read_xls as readXlsUtils
import src.base.calc_index.calSingleIndex as calUtils

import src.base.constans.Export as exportEnum
import src.base.constans.Finance as financeEnum

'''
用于计算常用的指标
'''

# 获取通用数据结构
def getCommonData(code):
    data = {}
    for financeName, financeMem in financeEnum.Finance.__members__.items():
        firstKey = code + '_' + financeName
        secondData = {}
        for exportName, exportMem in exportEnum.Export.__members__.items():
            print(code, ' 代码', exportName, ' 类型', financeName, ' 报告年限')
            secondKey = exportName
            dataXml = readXlsUtils.getCurrentFileContext(exportName, financeName, code)
            secondData[secondKey] = dataXml
        data[firstKey] = secondData
    print('整理好的数据：', data),
    return data

def calAllIndex(code, data):
    # 分成三种类型分别计算 report, simple, year
    for financeName, financeMem in financeEnum.Finance.__members__.items():
        firstKey = code + '_' + financeName
        for dateTime in data[firstKey]['debt']['datetime']:
            print('当前计算的时间为：', dateTime)
            callAllIndexFuc(data[firstKey][exportEnum.Export.benefit.value]['subject'],
                                               data[firstKey][exportEnum.Export.benefit.value][dateTime],
                                               data[firstKey][exportEnum.Export.debt.value]['subject'],
                                               data[firstKey][exportEnum.Export.debt.value][dateTime])
# 计算所有指标
def callAllIndexFuc(benefitSubject, benefitData, debtSubject, debtData):
    # 计算财务费用
    calUtils.calFinanceExpense(benefitSubject, benefitData)
    # 计算管理费用
    calUtils.calAdministrationExpense(benefitSubject, benefitData)
    # 计算销售费用
    calUtils.calSelledExpense(benefitSubject, benefitData)
    # 计算营业成本
    calUtils.calOperatingCost(benefitSubject, benefitData)
    # 计算所得税
    calUtils.calIncomeTax(benefitSubject, benefitData)
    # 计算其他利润 = 营业外收入 - 营业外支出
    calUtils.calOtherOperatingProfit(benefitSubject, benefitData)
    # 计算总成本
    calUtils.calTotalOperatingCost(benefitSubject, benefitData)
    # 计算营业总收入
    calUtils.calGrossRevenue(benefitSubject, benefitData)
    # 计算存货
    calUtils.calStock(debtSubject, debtData)
    # 计算应收账款
    calUtils.calReceiveCredit(debtSubject, debtData)
    # 计算货币资金
    calUtils.calCurrencyMoney(debtSubject, debtData)
    # 计算净利润
    calUtils.calRetainedProfits(benefitSubject, benefitData)
    # 计算非流动资产
    calUtils.calTotalNoncurrentAssets(debtSubject, debtData)
    # 计算流动资产
    calUtils.calFlowAssetCount(debtSubject, debtData)
    # 计算非流动负债
    calUtils.calTotalNoncurrentLiabilities(debtSubject, debtData)
    # 计算流动负债
    calUtils.calTotalCurrentLiabilities(debtSubject, debtData)
    # 计算总资产周转率 = 营业收入/资产总计
    calUtils.calTotalAssetsTurnover(benefitSubject, benefitData, debtSubject, debtData)
    # 计算销售净利率 = 净利润/营业总收入 净利润=利润总额-所得税
    calUtils.calNetProfitMarginOnSales(benefitSubject, benefitData)
    # 计算资产总额
    calUtils.calTotalAssets(debtSubject, debtData)
    # 计算负债总额
    calUtils.calTotalLiabilities(debtSubject, debtData)
    # 计算总资产收益率 = 销售净利率 * 总资产周转率
    calUtils.calReturnOnTotalAssets(benefitSubject, benefitData, debtSubject, debtData)
    # 计算权益乘数 = 资产总额 / 所有者权益总额（股东权益合计）
    calUtils.calEquityMultiplier(debtSubject, debtData)
    # 计算资产负债率 = 负债总额/资产总额
    calUtils.calAssetLiabilityRatio(debtSubject, debtData)
    # 计算净资产收益率 = 权益乘数 * 总资产收益率
    calUtils.calReturnOnEquity(benefitSubject, benefitData, debtSubject, debtData)
    # 计算股东权益合计
    calUtils.calTotalShareHolderSequity(debtSubject, debtData)

if __name__ == '__main__':
    calAllIndex('002078', getCommonData('002078'))
    # data = getCommonData('002078')
    # print(data['002078_report']),
    # # 计算财务费用
    # calSingleIndexUtils.calFinanceExpense(data['002078_report']['benefit']['subject'],
    #                                       data['002078_report']['benefit']['2018-03-31'])
    # # 计算管理费用
    # calSingleIndexUtils.calAdministrationExpense(data['002078_report']['benefit']['subject'],
    #                                              data['002078_report']['benefit']['2018-03-31'])
    # # 计算销售费用
    # calSingleIndexUtils.calSelledExpense(data['002078_report']['benefit']['subject'],
    #                                      data['002078_report']['benefit']['2018-03-31'])
    # # 计算其他利润 = 营业外收入 - 营业外支出
    # calSingleIndexUtils.calOtherOperatingProfit(data['002078_report']['benefit']['subject'],
    #                                             data['002078_report']['benefit']['2018-03-31'])
    # # 计算总资产周转率 = 营业收入/资产总计
    # calSingleIndexUtils.calTotalAssetsTurnover(data['002078_report']['benefit']['subject'],
    #                                            data['002078_report']['benefit']['2018-03-31'],
    #                                            data['002078_report']['debt']['subject'],
    #                                            data['002078_report']['debt']['2018-03-31'])
    # 计算总资产收益率
    # calSingleIndexUtils.calReturnOnTotalAssets(data['002078_report']['benefit']['subject'],
    #                                            data['002078_report']['benefit']['2018-03-31'],
    #                                            data['002078_report']['debt']['subject'],
    #                                            data['002078_report']['debt']['2018-03-31'])

    # 计算营业总收入
    # calSingleIndexUtils.calGrossRevenue(data['002078_report']['benefit']['subject'],
    #                                             data['002078_report']['benefit']['2018-03-31'])
    # # 计算净利润
    # calSingleIndexUtils.calRetainedProfits(data['002078_report']['benefit']['subject'],
    #                                     data['002078_report']['benefit']['2018-03-31'])
    #
    # calSingleIndexUtils.calNetProfitMarginOnSales(data['002078_report']['benefit']['subject'],
    #                                     data['002078_report']['benefit']['2018-03-31'])

    # 计算权益乘数
    # calSingleIndexUtils.calEquityMultiplier(data['002078_report']['debt']['subject'],
    #                                         data['002078_report']['debt']['2018-03-31'])
    # # 计算资产负债率
    # calSingleIndexUtils.calAssetLiabilityRatio(data['002078_report']['debt']['subject'],
    #                                             data['002078_report']['debt']['2018-03-31'])
    # 计算净资产收益率
    # calSingleIndexUtils.calReturnOnEquity(data['002078_report']['benefit']['subject'],
    #                                            data['002078_report']['benefit']['2018-03-31'],
    #                                            data['002078_report']['debt']['subject'],
    #                                            data['002078_report']['debt']['2018-03-31'])