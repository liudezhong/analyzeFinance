# -*- coding: UTF-8 -*-
import requests

import src.base.commons.commonUtils as commonUtils
import src.base.constans.Url as UrlEnum
import src.base.file_utils.fileUtils as fileUtils
import src.base.constans.StockBelongs as stockBeEnum
from urllib import request


# 从互联网获取获取文件
def obtainDataFromUrl(export, code):
    # 转换下载地址
    downFileUrl = UrlEnum.Url.down_ths.value + code + '_' + export + '.json'
    print('抓取信息url：' + downFileUrl)
    # 定义文件名
    filePathName = commonUtils.getCurrentFilePath(export, None, code, True)
    print('总体文件名：' + filePathName)
    response = requests.get(downFileUrl, headers=UrlEnum.Url.send_headers.value)

    with open(filePathName, 'w', encoding='utf-8') as f1:
        y = response.content.decode()
        z = y.replace('{\\', '{').replace('\\"', '"').replace('\\\\', '\\').replace('\"{', '{').replace('}\"', '}')
        f1.write(z)
    print('原始抓取文件写入original文件夹成功！')

# 根据code和所属访问新浪获取股票名称并处理
def obtainNameFromCode(code):
    response = requestSina(code, stockBeEnum.StockBelongs.SH.value)
    if (len(response.text.split('=')[1]) < 10):
        response = requestSina(code, stockBeEnum.StockBelongs.SZ.value)
    return response.text.split('=')[1].split(',')[0][1:]

# 根据code和所属访问新浪获取股票名称
def requestSina(code, belong):
    sinaUrl = UrlEnum.Url.sina_url.value + belong + code
    return requests.get(sinaUrl, headers=UrlEnum.Url.send_headers.value)

# 从同花顺获取信息并存入json文件中等待处理
def generatorOriginalFiles(code):
    # 初始化文件目录
    fileUtils.createFileDir(code)
    # 利润表
    obtainDataFromUrl('benefit', code)
    # 现金流量表
    obtainDataFromUrl('cash', code)
    # 资产负债表
    obtainDataFromUrl('debt', code)
    # 主要指标
    obtainDataFromUrl('main', code)
    # 每股能力
    obtainDataFromUrl('each', code)
    # 成长能力
    obtainDataFromUrl('grow', code)
    # 偿债能力
    obtainDataFromUrl('pay', code)
    # 运营能力
    obtainDataFromUrl('operate', code)

# 爬取股东分析页面
def obtainHtmlFromNetease(code, type):
    typeCode = type + '_' + code
    netEaseUrl = UrlEnum.Url.netease_url.value.replace('Code', typeCode)
    page = request.Request(netEaseUrl, headers=UrlEnum.Url.send_headers.value)
    request.urlopen(page).read().decode('utf-8')
    return request.urlopen(page).read().decode('utf-8')

# 获取历史交易数据
def obtainHistoricalTransactionData(code):
    pass

if __name__ =='__main__':
    # generatorOriginalFiles('002024')
    # print(obtainHtmlFromNetease('002024', 'gdfx'))
    print(obtainNameFromCode('002024'))