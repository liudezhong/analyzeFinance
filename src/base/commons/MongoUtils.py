# -*- coding: UTF-8 -*-
import copy
import datetime
import src.base.obtain_data.obtainData as obtainUtils

# 返回股票入库模板
def createStockTemp(code, industry):
    name = obtainUtils.obtainNameFromCode(code)
    stockTemp = {'stock':code, 'name': name, 'industry':industry, 'createTime': datetime.datetime.now(), 'updateTime': datetime.datetime.now(),
                   'updateCount': 0, 'status': 0}
    return copy.deepcopy(stockTemp)

