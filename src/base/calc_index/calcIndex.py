# -*- coding: UTF-8 -*-

import src.base.read_data.read_xls as readXlsUtils
import src.base.calc_index.calSingleIndex as calSingleIndexUtils

import src.base.constans.Export as exportEnum
import src.base.constans.Finance as financeEnum

'''
用于计算常用的指标
'''


# 获取通用数据
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


if __name__ == '__main__':
    data = getCommonData('002078')
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