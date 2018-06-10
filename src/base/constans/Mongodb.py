# -*- coding: UTF-8 -*-

from enum import Enum

# mongodb的主要参数
class Mongodb(Enum):
    MongoUrl = '127.0.0.1:27017'
    Database = 'analysis'
    # 存储历史交易数据
    CollectionStock = 'stock'
    # 存储财务数据
    CollectionFinancial = 'financial'
    # 存储指标数据
    CollectionIndex = 'index'
    # 存储比率数据
    CollectionRadio = 'radio'
