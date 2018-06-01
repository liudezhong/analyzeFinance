# -*- coding: UTF-8 -*-
import src.base.commons.CommonUtils as commonUtils
import src.base.constans.Type as typeEnum
import src.base.constans.Export as exportEnum
import src.base.constans.IndustryContrast as inContastEnum
import src.base.commons.MongoUtils as mongoUtils
import src.base.db.mongodb as mongoDb
import json
import xlwt

import src.base.obtain_data.obtainData as obtainDataUtils


#用于将原始数据处理到excel表格中
def singleHandleJsonToExcel(export, code):
    # 获取文件目录的位置
    filePathName = commonUtils.getCurrentFilePath(export, None, code, True)
    print('读取当前文件名为：', filePathName)
    with open(filePathName, 'r') as f:
        data = json.load(f)
    for name, member in typeEnum.Type.__members__.items():
        if (name != typeEnum.Type.original.value):
            excelFileName = commonUtils.getCurrentFilePath(export, member.value, code, False)
            print('写入excel文件：', excelFileName, '开始', 'title = ', data['flashData']['title']),
            processDataToExcel(data['flashData']['title'], data['flashData'][member.value], export, excelFileName)
            print('写入excel文件：', excelFileName, '结束', 'value = ', data['flashData'][member.value])
            # 财务数据入库开始
            print('财务数据入库：', excelFileName, '开始', 'title = ', data['flashData']['title']),
            processDataToMongo(data['flashData']['title'], data['flashData'][member.value], member.value, export, code)
            print('财务数据入库：', excelFileName, '结束', 'value = ', data['flashData'][member.value])


# 财务数据入库
def processDataToMongo(titles, datas, typeData, export, code):
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
    stockTemp[export + '_' + typeData + '_title'] = titles
    stockTemp[export + '_' + typeData + '_time'] = datas[0]
    distExport = {}
    # 组装数据
    for data in datas[0]:
        for da in datas[1:]:
            distExport[str(data)] = da
    stockTemp[export + '_' + typeData + '_data'] = distExport
    dbUtil = mongoDb.getFinancialDb()
    if dbUtil.find({'stock': code}).count() > 0:
        dbUtil.delete_many({'stock': code, 'export': export, 'type': typeData})
    dbUtil.insert_one(stockTemp)

# 添加数据到excel
def processDataToExcel(titleData, data, export, excelFileName):
    title = xlwt.Workbook()  # 创建excel对象
    sheet = title.add_sheet(export, cell_overwrite_ok=True)  # 添加一个表
    c = 0  # 保存当前列
    for t in titleData:  # 取出data中的每一个元组存到表格的每一行
        sheet.write(c, 0, processTile(t))
        c += 1
    c = 0  # 保存当前列
    for d in data:  # 取出data中的每一个元组存到表格的每一行
        for index in range(len(d)):  # 将每一个元组中的每一个单元存到每一列
            sheet.write(c, index+1, d[index])
        c += 1
    title.save(excelFileName)  # 保存excel

# 组装首列
def processTile(data):
    if (isinstance(data, list)):
        return data[0] + '(' + data[1] + ')'
    return data

def allHandleDataToExcel(code):
    for name, member in exportEnum.Export.__members__.items():
        print('处理', member.value, '写入excel并写入mongo库开始')
        singleHandleJsonToExcel(member.value, code)
        print('处理', member.value, '写入excel并写入mongo库结束')

if __name__ =='__main__':
    allHandleDataToExcel('002024'),