# -*- coding: UTF-8 -*-
import src.base.commons.commonUtils as commons
import src.base.constans.CalcIndex as CalcIndexEnum
import src.base.constans.Constans as consEnum
import xlwt
import xlrd
from xlutils.copy import copy

# 打开对应的excel，写入对应的数据
def handleIndexTemplateToExcel(datetime, export, type, code):
    excelDist = {}
    #获取文件
    filePath = commons.getAnalysisFilePath(export, type, code)
    excelDist['filePath'] = filePath
    title = xlwt.Workbook()  # 创建excel对象
    sheet = title.add_sheet(export, cell_overwrite_ok=True)  # 添加一个表
    sheet.write(0, 0, '科目/日期')
    # 标题写入文件
    c = 1
    for date in datetime:
        sheet.write(0, c, date)
        c += 1
    # 时间写入文件
    c = 1
    for name, member in CalcIndexEnum.CalcIndex.__members__.items():
        print('member.value', member.value),
        sheet.write(c, 0, member.value)
        c += 1
    print('filePath = ', filePath),
    excelDist['title'] = title
    excelDist['sheet'] = sheet
    # title.save(filePath)  # 保存excel
    return excelDist

# 存入数据
def handleDataToExcel(data, col, export, excelDist):
    c = 1
    for index in data:
        print('index', index),
        excelDist['sheet'].write(c, col, index)
        c += 1
    excelDist['title'].save(excelDist['filePath'])

# 打开对应的excel，写入对应的数据
def handleSpecialIndexToExcel(df, dataList, export, type, code, specialName):
    #获取文件
    filePath = commons.getAnalysisFilePath(export, type, code)
    src = xlrd.open_workbook(filePath, formatting_info=True)
    sheetOld = src.sheet_by_index(0)
    destination = copy(src)
    sheet = destination.add_sheet(specialName)
    # 标题写入文件
    x = df.columns.values.tolist()[0:consEnum.Constans.PlotXSpan.value]
    c = 0
    for date in x:
        sheet.write(0, c, date)
        c += 1
    # 时间写入文件
    c = 1
    for da in dataList:
        rowsData = sheetOld.row_values(da + 1)[0:consEnum.Constans.PlotXSpan.value]
        d = 0
        for rowData in rowsData:
            sheet.write(c, d, rowData)
            d += 1
        c += 1
    destination.save(filePath)  # 保存excel
