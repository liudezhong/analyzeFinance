# -*- coding: UTF-8 -*-
import xlrd
import xlwt
from xlutils.copy import copy

import src.base.commons.CommonUtils as commons
import src.base.commons.MongoUtils as mongoUtils
import src.base.constans.CalcIndex as CalcIndexEnum
import src.base.constans.Constans as consEnum
import src.base.constans.IndustryContrast as inContastEnum
import src.base.db.mongodb as mongoDb
import src.base.obtain_data.obtainData as obtainDataUtils


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

# 财务指标数据入库
def processDataToMongo(times, datas, typeData, export, code):
    distData = {}
    codeName = obtainDataUtils.obtainNameFromCode(code)
    # 获取是上海还是深圳
    codeType = obtainDataUtils.determineLocation(code)
    # 获取行业数据
    industryInfo = obtainDataUtils.obtainIndustryInfo(code)
    # 创建mongo模板
    stockTemp = mongoUtils.createStockTemp(code)
    # 放入数据
    stockTemp['name'] = codeName
    stockTemp['hisTransName'] = codeName
    stockTemp['address'] = codeType
    stockTemp[inContastEnum.IndustryContrast.industry.name] = industryInfo[inContastEnum.IndustryContrast.industry.name]
    stockTemp[inContastEnum.IndustryContrast.upcompany.name] = industryInfo[
        inContastEnum.IndustryContrast.upcompany.name]
    stockTemp[inContastEnum.IndustryContrast.regional.name] = industryInfo[inContastEnum.IndustryContrast.regional.name]
    stockTemp['export'] = export
    stockTemp['type'] = typeData
    # 获取标题数据
    titles = []
    for name, member in CalcIndexEnum.CalcIndex.__members__.items():
        titles.append(member.value)
    stockTemp[export + '_' + typeData + '_title'] = titles
    stockTemp[export + '_' + typeData + '_time'] = times
    # 组装数据
    stockTemp[export + '_' + typeData + '_data'] = datas
    dbUtil = mongoDb.getIndexDb()
    if dbUtil.find({'stock': code, 'export': export, 'type': typeData}).count() > 0:
        dbUtil.delete_many({'stock': code, 'export': export, 'type': typeData})
    dbUtil.insert_one(stockTemp)

# 存入数据
def handleDataToExcel(data, col, export, excelDist):
    c = 1
    for index in data:
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
