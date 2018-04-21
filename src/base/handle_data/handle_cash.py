# -*- coding: UTF-8 -*-
import src.base.commons.commonUtils as commonUtils
import json

'''
用于将原始数据处理到excel表格中
'''

def processJsonToExcel(export, type, code):
    # 获取文件目录的位置
    filePathName = commonUtils.getCurrentFilePath(export, type, code)
    with open(filePathName, 'r') as f:
        data = json.load(f)
    print (data['flashData']['title'])
if __name__ =='__main__':
    print(processJsonToExcel('benefit', 'year', '002024'))