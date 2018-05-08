# -*- coding: UTF-8 -*-

import src.base.read_data.read_xls as readXlsUtils
import src.base.calc_index.calSingleIndex as calUtils
import src.base.handle_data.handleIndexToExcel as handleUtils

import src.base.constans.Export as exportEnum
import src.base.constans.Finance as financeEnum
import src.base.constans.Analysis as analysisEnum

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


def calAllIndex(code):
    data = getCommonData(code)
    # 分成三种类型分别计算 report, simple, year
    for financeName, financeMem in financeEnum.Finance.__members__.items():
        firstKey = code + '_' + financeName
        # 生成模板类文件
        handleUtils.handleIndexTemplateToExcel(data[firstKey][exportEnum.Export.benefit.value]['datetime'],
                                               analysisEnum.Analysis.analysis.value, financeName,
                                               code)
        col = 1
        app = handleUtils.getAppObject()
        wb = handleUtils.getWbObject(analysisEnum.Analysis.analysis.value, financeMem.value, code, app)
        for dateTime in data[firstKey]['debt']['datetime']:
            print('当前计算的时间为：', dateTime)
            indexList = callAllIndexFuc(data[firstKey][exportEnum.Export.benefit.value]['subject'],
                             data[firstKey][exportEnum.Export.benefit.value][dateTime],
                             data[firstKey][exportEnum.Export.debt.value]['subject'],
                             data[firstKey][exportEnum.Export.debt.value][dateTime])
            handleUtils.handleDataToExcel(indexList, col, analysisEnum.Analysis.analysis.value, wb)
            col += 1
        handleUtils.closeWbObject(wb, app)


# 计算所有指标
def callAllIndexFuc(benefitSubject, benefitData, debtSubject, debtData):
    indexList = []
    # 计算财务费用
    indexList.append(calUtils.calFinanceExpense(benefitSubject, benefitData))
    # 计算管理费用
    indexList.append(calUtils.calAdministrationExpense(benefitSubject, benefitData))
    # 计算销售费用
    indexList.append(calUtils.calSelledExpense(benefitSubject, benefitData))
    # 计算营业成本
    indexList.append(calUtils.calOperatingCost(benefitSubject, benefitData))
    # 计算所得税
    indexList.append(calUtils.calIncomeTax(benefitSubject, benefitData))
    # 计算其他利润 = 营业外收入 - 营业外支出
    indexList.append(calUtils.calOtherOperatingProfit(benefitSubject, benefitData))
    # 计算总成本
    indexList.append(calUtils.calTotalOperatingCost(benefitSubject, benefitData))
    # 计算营业总收入
    indexList.append(calUtils.calGrossRevenue(benefitSubject, benefitData))
    # 计算存货
    indexList.append(calUtils.calStock(debtSubject, debtData))
    # 计算应收账款
    indexList.append(calUtils.calReceiveCredit(debtSubject, debtData))
    # 计算货币资金
    indexList.append(calUtils.calCurrencyMoney(debtSubject, debtData))
    # 计算净利润
    indexList.append(calUtils.calRetainedProfits(benefitSubject, benefitData))
    # 计算非流动资产
    indexList.append(calUtils.calTotalNoncurrentAssets(debtSubject, debtData))
    # 计算流动资产
    indexList.append(calUtils.calFlowAssetCount(debtSubject, debtData))
    # 计算非流动负债
    indexList.append(calUtils.calTotalNoncurrentLiabilities(debtSubject, debtData))
    # 计算流动负债
    indexList.append(calUtils.calTotalCurrentLiabilities(debtSubject, debtData))
    # 计算总资产周转率 = 营业收入/资产总计
    indexList.append(calUtils.calTotalAssetsTurnover(benefitSubject, benefitData, debtSubject, debtData))
    # 计算销售净利率 = 净利润/营业总收入 净利润=利润总额-所得税
    indexList.append(calUtils.calNetProfitMarginOnSales(benefitSubject, benefitData))
    # 计算股东权益合计
    indexList.append(calUtils.calTotalShareHolderSequity(debtSubject, debtData))
    # 计算资产总额
    indexList.append(calUtils.calTotalAssets(debtSubject, debtData))
    # 计算负债总额
    indexList.append(calUtils.calTotalLiabilities(debtSubject, debtData))
    # 计算总资产收益率 = 销售净利率 * 总资产周转率
    indexList.append(calUtils.calReturnOnTotalAssets(benefitSubject, benefitData, debtSubject, debtData))
    # 计算权益乘数 = 资产总额 / 所有者权益总额（股东权益合计）
    indexList.append(calUtils.calEquityMultiplier(debtSubject, debtData))
    # 计算资产负债率 = 负债总额/资产总额
    indexList.append(calUtils.calAssetLiabilityRatio(debtSubject, debtData))
    # 计算净资产收益率 = 权益乘数 * 总资产收益率
    indexList.append(calUtils.calReturnOnEquity(benefitSubject, benefitData, debtSubject, debtData))

    return indexList


if __name__ == '__main__':
    calAllIndex('002078')
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
