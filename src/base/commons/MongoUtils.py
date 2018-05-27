# -*- coding: UTF-8 -*-
import copy
import datetime


# 返回股票入库模板
def createStockTemp(code):
    stockTemp = {'stock': code, 'name': '', 'industry': '', 'upcompany': 0, 'regional': '', 'createTime': datetime.datetime.now(), 'updateTime': datetime.datetime.now(),
                 'hisTransData': {}, 'hisTransName': [], 'updateCount': 0, 'status': 0}
    return copy.deepcopy(stockTemp)
