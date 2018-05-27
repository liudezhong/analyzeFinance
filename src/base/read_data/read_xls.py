# -*- coding: UTF-8 -*-
import xlrd

import src.base.commons.CommonUtils as commUtils
import src.base.constans.Finance as FinanceEnum
import src.base.constans.Export as exportEnum


# 读取excel文件
def readXls(filePath):
    excelFile = xlrd.open_workbook(filePath, 'r')
    table = excelFile.sheet_by_index(0)
    return table

# 整理数据，将数据整理成可用的状态
def tidyData(table):
    rowSize = len(table.row_values(0)) - 1
    colSize = len(table.col_values(0)) - 1
    tidyDist = {}
    # 整理所有列的财务数据项
    element = 'subject' #table.cell(0, 0).value
    elements = []
    for j in range(colSize):
        elements.append(table.cell(j + 1, 0).value)
    tidyDist[element] = elements
    # 整理所有日期项
    element = 'datetime'
    elements = []
    for k in range(rowSize):
        elements.append(table.cell(0, k + 1).value)
    tidyDist[element] = elements
    # 整理内容数据
    for i in range(rowSize):
        element = table.cell(0, i + 1).value
        elements = []
        for j in range(colSize):
            elements.append(table.cell(j + 1,i + 1).value)
        tidyDist[element] = elements
    print('整理数据结果：', tidyDist),
    return tidyDist

# 读取固定目录下的文件内容并整理成dist格式
def getCurrentFileContext(exprot, type, code):
    return tidyData(readXls(commUtils.getCurrentFilePath(exprot, type, code, False)))

if __name__ =='__main__':
    getCurrentFileContext(exportEnum.Export.debt._name_, FinanceEnum.Finance.report._name_, '002078')

