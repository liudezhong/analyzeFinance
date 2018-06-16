# -*- coding: UTF-8 -*-

import src.base.db.mongodb as mongoDb
import src.base.constans.Analysis as analysisEnum
import src.base.constans.Type as typeEnum
import src.base.commons.DateUtils as dateUtils
import src.base.calc_index.calValueIndex as calValueIndexUtils

import datetime

# 使用折现现金流模型进行估值
def calDiscountedCashFlow(code):
    # 获取当前的年度的自由现金流
    dbUtil = mongoDb.getIndexDb()
    param = {'stock': code, 'export': analysisEnum.Analysis.analysis.value, 'type': typeEnum.Type.year.value}
    data = dbUtil.find_one(param)['analysis_year_data']
    # 获取上个年份
    lastYear = dateUtils.getLastYear(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # 获取自由现金流
    freeCashFlow = data[lastYear][25]
    print('freeCashFlow = ', freeCashFlow)
    # todo 假设增长率不变，维持在5%
    growthRate = 0.05
    # todo 下一个10年的自由现金流
    nextTenYearCashFlows = []
    nextTenYearCashFlow = freeCashFlow
    for i in range(1, 11, 1):
        nextTenYearCashFlow = nextTenYearCashFlow * (1 + growthRate)
        nextTenYearCashFlows.append(nextTenYearCashFlow)
    print('nextTenYearCashFlows = ', nextTenYearCashFlows)
    # TODO 折现率
    discountRate = 0.09
    # todo 折现成现值
    discountedPresentValues = []
    for i in range(1, 11, 1):
        discountedPresentRate = (1 + discountRate) ** i
        discountedPresentValues.append(nextTenYearCashFlows[i - 1]/discountedPresentRate)
    print('discountedPresentValues = ', discountedPresentValues)
    # todo 年增长率
    annualGrowthRate = 0.03
    # todo 计算永续年金价值
    perpetuityValue = nextTenYearCashFlows[9] * (1 + annualGrowthRate) / (discountRate - annualGrowthRate)
    print('计算永续年金价值 perpetuityValue = ', perpetuityValue)
    # 折现
    discount = perpetuityValue / (1 + discountRate) ** 10
    print('折现 discount = ', discount)
    # 计算所有者权益
    countNextTenYearCashFlows = 0
    for i in range(10):
        countNextTenYearCashFlows += nextTenYearCashFlows[i]
    totalOwnersEquity = countNextTenYearCashFlows + discount
    print('所有者权益合计 totalOwnersEquity = ', totalOwnersEquity)
    valuePerShare = totalOwnersEquity / calValueIndexUtils.calCirculateCount(code)['circulateCount']
    print('计算每股价值：', valuePerShare)
    # 更新每股价值
    dbUtil = mongoDb.getStockDb()
    dbUtil.update({'stock': code}, {'$set': {'valuePerShare': valuePerShare}})

if __name__ == '__main__':
    calDiscountedCashFlow('600600')