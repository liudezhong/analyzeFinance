# -*- coding: UTF-8 -*-
import src.base.commons.commonUtils as commonUtils
import src.base.constans.Type as typeEnum
import src.base.constans.Export as exportEnum
import json
import xlwt


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
            print('写入excel文件：', excelFileName, '开始'),
            processDataToExcel(data['flashData']['title'], data['flashData'][member.value], export, excelFileName)
            print('写入excel文件：', excelFileName, '结束')

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
        print('处理', member.value, '写入excel开始')
        singleHandleJsonToExcel(member.value, code)
        print('处理', member.value, '写入excel结束')

if __name__ =='__main__':
    allHandleDataToExcel('002024'),