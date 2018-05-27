# -*- coding: UTF-8 -*-
import requests

import src.base.commons.CommonUtils as commonUtils
import src.base.commons.DateUtils as dateUtils
import src.base.constans.Url as UrlEnum
import src.base.file_utils.fileUtils as fileUtils
import src.base.constans.StockBelongs as stockBeEnum
import src.base.commons.MongoUtils as mongoUtils
import src.base.db.mongodb as mongoDb
import src.base.constans.IndustryContrast as inContastEnum
import src.base.constans.HisTransData as hisTransDataEnum

from bs4 import BeautifulSoup
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

# 判断是上海还是深圳
def determineLocation(code):
    response = requestSina(code, stockBeEnum.StockBelongs.SH.value)
    if (len(response.text.split('=')[1]) < 10):
        return stockBeEnum.StockBelongs.sz.value
    return stockBeEnum.StockBelongs.sh.value

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

# 获取所属行业数据
def obtainIndustryInfo(code):
    industryUrl = UrlEnum.Url.industry_url.value.replace('CODE', code)
    page = request.Request(industryUrl, headers=UrlEnum.Url.send_headers.value)
    page_info = request.urlopen(page).read().decode('utf-8')
    soup = BeautifulSoup(page_info, 'lxml')
    divs = soup.findAll('div', class_='inner_box industry_info')
    dataDist = {}
    for div in divs:
        for span in div.findAll('span'):
            if span.strong.getText().find(inContastEnum.IndustryContrast.industry.value) >= 0:
                dataDist[inContastEnum.IndustryContrast.industry.name] = span.em.a.getText().strip()
            elif span.strong.getText().find(inContastEnum.IndustryContrast.upcompany.value) >= 0:
                dataDist[inContastEnum.IndustryContrast.upcompany.name] = span.em.getText().strip()
            elif span.strong.getText().find(inContastEnum.IndustryContrast.regional.value) >= 0:
                dataDist[inContastEnum.IndustryContrast.regional.name] = span.em.a.getText().strip()
            else:
                pass
    return dataDist

# 获取历史交易数据
def obtainHistoricalTransactionData(code):
    # 计算时间
    beginDate = str(dateUtils.getYear(-11)) + '-01-01'
    monthList = dateUtils.getBetweenMonth(beginDate)
    codeName = obtainNameFromCode(code)
    # 获取是上海还是深圳
    codeType = determineLocation(code)
    # 获取行业数据
    industryInfo = obtainIndustryInfo(code)
    # 创建mongo模板
    stockTemp = mongoUtils.createStockTemp(code)
    # 放入数据
    stockTemp['name'] = codeName
    stockTemp['hisTransName'] = codeName
    stockTemp[inContastEnum.IndustryContrast.industry.name] = industryInfo[inContastEnum.IndustryContrast.industry.name]
    stockTemp[inContastEnum.IndustryContrast.upcompany.name] = industryInfo[inContastEnum.IndustryContrast.upcompany.name]
    stockTemp[inContastEnum.IndustryContrast.regional.name] = industryInfo[inContastEnum.IndustryContrast.regional.name]
    stockTemp['hisTransName'] = hisTransDataEnum.HisTransData.Cols.value
    monthData = {}
    for month in monthList:
        startDate = month + '01'
        endDate = month + '31'
        netEaseChddataUrl = UrlEnum.Url.netEase_chddata_url.value.replace('TYPE', codeType).replace('CODE', code) \
            .replace('START', startDate).replace('END', endDate)

        data = requests.get(netEaseChddataUrl)
        transMonthData = []
        if len(data.text.split('\r\n')) > 2:
            for da in data.text.split('\r\n'):
                if da != '' and not da.startswith('日期'):
                    transData = {da.split(',')[0]: da.split(',')[1:]}
                    transMonthData.append(transData)
        if len(transMonthData) > 0:
            monthData[month] = transMonthData
    stockTemp['hisTransData'] = monthData
    dbUtil = mongoDb.initDb()
    if dbUtil.find({'stock': code}).count() > 0:
        dbUtil.delete_many({'stock': code})
    print(stockTemp)
    dbUtil.insert_one(stockTemp)





if __name__ =='__main__':
    # generatorOriginalFiles('002024')
    # print(obtainHtmlFromNetease('002024', 'gdfx'))
    # print(obtainNameFromCode('002024'))
    obtainHistoricalTransactionData('603589')
    # obtainIndustryInfo('603589')
