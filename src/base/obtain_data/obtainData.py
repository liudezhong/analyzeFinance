# -*- coding: UTF-8 -*-
import requests
import json
from urllib import request
import src.base.constans.Url as UrlEnum
import src.base.constans.File as FileEnum
import src.base.commons.commonUtils as commonUtils

# 从互联网获取获取文件
def obtainDataFromUrl(export, type, code):
    # 转换下载地址
    downFileUrl = UrlEnum.Url.down_ths.value + code + '_' + export + '.json'
    # downFileUrl = 'http://basic.10jqka.com.cn/api/stock/finance/002024_cash.json'
    # 定义文件存储位置
    fileName = export + '.json'
    filePath = FileEnum.File.FinanceFile.value + code + '\\' + type + '\\'
    filePathName = filePath + fileName
    print(filePathName)
    commonUtils.mkdir(filePath)
    print(downFileUrl)
    response = requests.get(downFileUrl, headers=UrlEnum.Url.send_headers.value)

    with open(filePathName, 'w', encoding='utf-8') as f1:
        y = response.content.decode()
        z = y.replace('{\\', '{').replace('\\"', '"').replace('\\\\', '\\').replace('\"{', '{').replace('}\"', '}')
        f1.write(z)
        a = json.loads(z)
        print(a)

# 从同花顺获取信息并存入相应的表格中等待处理
def generatorOriginalFiles(code):
    # 利润表
    obtainDataFromUrl('benefit', 'year', code)
    # 现金流量表
    obtainDataFromUrl('cash', 'year', code)
    # 资产负债表
    obtainDataFromUrl('debt', 'year', code)

if __name__ =='__main__':
    generatorOriginalFiles('002024')