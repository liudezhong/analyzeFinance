# -*- coding: UTF-8 -*-
import src.base.constans.Cash as cash
import xlrd
import os

# 读取excel文件
def readXls(filePath):
    excelFile = xlrd.open_workbook(filePath)
    table = excelFile.sheet_by_index(0)
    return table

# 读取excel目录下的所有文件
def readFiles(path):
    needFiles = [];
    for root, dirs, files in os.walk(path):
        if len(files) > 0:
            for file in files:
                if file.endswith('.xls'):
                    needFiles.append(file)
    return needFiles

if __name__ =='__main__':
    files = readFiles("/Users/fanpu/developer/资金/苏宁易购")
    print(cash.Cash.BusiAmount.value)


