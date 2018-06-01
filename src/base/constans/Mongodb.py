# -*- coding: UTF-8 -*-

from enum import Enum

# mongodb的主要参数
class Mongodb(Enum):
    MongoUrl = '127.0.0.1:27017'
    Database = 'analysis'
    CollectionStock = 'stock'
    CollectionFinancial = 'financial'
