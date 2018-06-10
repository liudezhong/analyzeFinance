# -*- coding: UTF-8 -*-

import src.base.db.mongodb as mongoDb
import src.base.constans.Type as typeEnum
import src.base.constans.Analysis as analysisEnum
import src.base.commons.DateUtils as dateUtils
import src.base.commons.CommonUtils as commUtils

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


# 计算市盈率
def calPERatio():
    dbUtil = mongoDb.getIndexDb()
    pass

# 计算市净率
def calPriceToBook():
    dbUtil = mongoDb.getIndexDb()
    pass

if __name__ == '__main__':
    calPriceToSalesRatio('002024')