# -*- coding: UTF-8 -*-

import src.base.db.mongodb as mongoDb
import src.base.constans.Type as typeEnum
import src.base.constans.Export as exportEnum
import src.base.constans.Analysis as analysisEnum
import src.base.commons.DateUtils as dateUtils
import src.base.commons.CommonUtils as commUtils
import src.base.constans.IndustryContrast as inContastEnum
import src.base.obtain_data.obtainData as obtainDataUtils
import src.base.commons.MongoUtils as mongoUtils

def calRatioToMongo(code):
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
    stockTemp['PriceToSalesRatio'] = calPriceToSalesRatio(code)
    stockTemp['PERatio'] = calPERatio(code)
    stockTemp['PriceToBook'] = calPriceToBook(code)
    dbUtil = mongoDb.getRadioDb()
    if dbUtil.find({'stock': code}).count() > 0:
        dbUtil.delete_many({'stock': code})
    dbUtil.insert_one(stockTemp)

# 计算市销率
def calPriceToSalesRatio(code):
    # 获取股票的指标数据
    dbUtil = mongoDb.getIndexDb()
    params = {'stock':code, 'type':typeEnum.Type.simple.value}
    indexs = dbUtil.find_one(params)
    indexDataFlag = analysisEnum.Analysis.analysis.value + '_' + typeEnum.Type.simple.value + '_data'
    indexTimeFlag = analysisEnum.Analysis.analysis.value + '_' + typeEnum.Type.simple.value + '_time'

    # 获取股票的交易数据
    dbUtil = mongoDb.getStockDb()
    del params['type']
    hisData = dbUtil.find_one(params)
    # 计算市销率
    distRatio = {}
    for hisMonthKey in hisData['hisTransData']:
        # print('hisMonthKey', hisMonthKey)
        listRatio = []
        for hisDayDate in hisData['hisTransData'][hisMonthKey]:
            # print(hisDayDate)
            # 计算总市值
            totalMarketValueLen = len(hisDayDate[list(hisDayDate.keys())[0]]) - 2
            totalMarketValue = commUtils.transMoney(hisDayDate[list(hisDayDate.keys())[0]][totalMarketValueLen])
            # print('totalMarketValue = ', totalMarketValue)
            # 计算当前营业总收入
            cardinalDate = dateUtils.getSomeIndexDay(list(hisDayDate.keys())[0], indexs[indexTimeFlag])
            cardinalData = indexs[indexDataFlag][cardinalDate][7]
            # print('cardinalData = ', cardinalData, 'cardinalDate = ', cardinalDate, 'list(hisDayDate.keys())[0] = ', list(hisDayDate.keys())[0])
            # 计算市销率
            priceToSalesRatio = commUtils.handleDivisionZero(totalMarketValue, cardinalData)
            # print('priceToSalesRatio = ', priceToSalesRatio)
            # 组装入库数据
            distPerRatio = {list(hisDayDate.keys())[0]: priceToSalesRatio}
            listRatio.append(distPerRatio)
        distRatio[hisMonthKey] = listRatio
    print('distRatio = ', distRatio)
    return distRatio


# 计算市盈率
def calPERatio(code):
    # 获取股票的指标数据
    dbUtil = mongoDb.getFinancialDb()
    params = {'stock': code, 'type': typeEnum.Type.year.value, 'export': exportEnum.Export.each.value}
    print(params)
    indexs = dbUtil.find_one(params)
    indexDataFlag = exportEnum.Export.each.value + '_' + typeEnum.Type.year.value + '_data'

    # 获取股票的交易数据
    dbUtil = mongoDb.getStockDb()
    del params['type']
    del params['export']
    hisData = dbUtil.find_one(params)
    # 计算市盈率
    distRatio = {}
    for hisMonthKey in hisData['hisTransData']:
        # print('hisMonthKey', hisMonthKey)
        listRatio = []
        for hisDayDate in hisData['hisTransData'][hisMonthKey]:
            # 计算当前股票的收盘价
            closeddPrice = commUtils.transMoney(hisDayDate[list(hisDayDate.keys())[0]][3])
            print('closeddPrice = ', closeddPrice)
            # 计算上一年的每股收益
            lastYear = dateUtils.getLastYear(list(hisDayDate.keys())[0])
            earningsPerShare = float(indexs[indexDataFlag][lastYear][0])
            print('indexs[indexDataFlag][lastYear] = ', indexs[indexDataFlag][lastYear], 'year = ', lastYear);
            print('earningsPerShare = ', earningsPerShare)
            # 计算市盈率
            peRatio = round(commUtils.handleDivisionZero(closeddPrice, earningsPerShare), 2)
            print('peRatio = ', peRatio, 'date', list(hisDayDate.keys())[0])
            # 组装入库数据
            distPerRatio = {list(hisDayDate.keys())[0]: peRatio}
            listRatio.append(distPerRatio)
        distRatio[hisMonthKey] = listRatio
    print('distRatio = ', distRatio)
    return distRatio

# 计算市净率
def calPriceToBook(code):
    # 获取股票的指标数据
    dbUtil = mongoDb.getFinancialDb()
    params = {'stock': code, 'type': typeEnum.Type.year.value, 'export': exportEnum.Export.each.value}
    print(params)
    indexs = dbUtil.find_one(params)
    indexDataFlag = exportEnum.Export.each.value + '_' + typeEnum.Type.year.value + '_data'

    # 获取股票的交易数据
    dbUtil = mongoDb.getStockDb()
    del params['type']
    del params['export']
    hisData = dbUtil.find_one(params)
    # 计算市盈率
    distRatio = {}
    for hisMonthKey in hisData['hisTransData']:
        # print('hisMonthKey', hisMonthKey)
        listRatio = []
        for hisDayDate in hisData['hisTransData'][hisMonthKey]:
            # 计算当前股票的收盘价
            closeddPrice = commUtils.transMoney(hisDayDate[list(hisDayDate.keys())[0]][3])
            print('closeddPrice = ', closeddPrice)
            # 计算上一年的每股净资产
            lastYear = dateUtils.getLastYear(list(hisDayDate.keys())[0])
            netAssetPerShare = float(indexs[indexDataFlag][lastYear][1])
            print('indexs[indexDataFlag][lastYear] = ', indexs[indexDataFlag][lastYear], 'year = ', lastYear);
            print('netAssetPerShare = ', netAssetPerShare)
            # 计算市净率
            priceToBook = round(commUtils.handleDivisionZero(closeddPrice, netAssetPerShare), 2)
            print('priceToBook = ', priceToBook, 'date', list(hisDayDate.keys())[0])
            # 组装入库数据
            distPerRatio = {list(hisDayDate.keys())[0]: priceToBook}
            listRatio.append(distPerRatio)
        distRatio[hisMonthKey] = listRatio
    print('distRatio = ', distRatio)
    return distRatio

if __name__ == '__main__':
    # calPriceToSalesRatio('002024')
    # calPERatio('002024')
    # calPriceToBook('002024')
    calRatioToMongo('002024')