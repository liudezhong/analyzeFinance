# -*- coding: UTF-8 -*-
import pymongo
import src.base.constans.Mongodb as mongodbEnum
import src.base.commons.MongoUtils as mUtils


'''
Stock
    stockCollection = {'stock':'000635', createTime: now(), updateTime: now(), updateCount:0}
    industryCollection = {'building': [{}, {}], 'food'：[{}, {}]}
'''

# mongodb初始化
def initDb():
    mongoUrl = mongodbEnum.Mongodb.MongoUrl.value
    dataBase = mongodbEnum.Mongodb.Database.value
    collection = mongodbEnum.Mongodb.Collection.value
    client = pymongo.MongoClient(mongoUrl)
    db = client[dataBase]
    # 返回数据库连接对象
    return db[collection]

# 根据code和行业初始化数据库
def initStock(code, industry):
    dbUtils = initDb()
    param = {'stock': code}
    if (dbUtils.find_one(param) != None):
        dbUtils.delete_many(param)
    stockTemp = mUtils.createStockTemp(code, industry)
    dbUtils.insert_one(stockTemp)


if __name__ == '__main__':
    initStock('600600', '饮料制造')
