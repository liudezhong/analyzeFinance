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
    print(data),
    return data


if __name__ =='__main__':
    data = getCommonData('002078')
    print(data['002078_report'])
    calSingleIndexUtils.calFinanceExpense(data['002078_report']['benefit']['2018-03-31'])
    calSingleIndexUtils.calAdministrationExpense(data['002078_report']['benefit']['2018-03-31'])
