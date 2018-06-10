# -*- coding: UTF-8 -*-

import datetime
import time
import calendar

# 遍历月份
def getBetweenMonth(beginDate):
    date_list = []
    begin_date = datetime.datetime.strptime(beginDate, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(time.strftime('%Y-%m-%d', time.localtime(time.time())), "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y%m")
        date_list.append(date_str)
        begin_date = addMonths(begin_date, 1)
    return date_list

# 增加月份
def addMonths(dt, months):
    month = dt.month - 1 + months
    year = int(dt.year + month / 12)
    month = month % 12 + 1
    day = min(dt.day, calendar.monthrange(year, month)[1])
    return dt.replace(year=year, month=month, day=day)

# 获取某一年
def getYear(interval):
    return int(datetime.datetime.now().strftime("%Y")) + interval

# 获取当天股票交易日对应的股票指标日期
def getSomeIndexDay(transDay, indexDays):
    if transDay >= indexDays[0]:
        return indexDays[0]
    elif transDay <= indexDays[len(indexDays) - 1]:
        return indexDays[len(indexDays) - 1]

    for index in range(len(indexDays) - 2):
        if transDay >= indexDays[index + 1] and transDay < indexDays[index]:
            return indexDays[index + 1]


if __name__ == '__main__':
    print(getBetweenMonth('2008-01-01'))
    print(getYear(5))

