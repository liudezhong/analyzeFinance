# -*- coding: UTF-8 -*-

from enum import Enum

class Finance(Enum):
    benefit = '利润表'
    cash = '现金流量表'
    debt = '资产负债表'
    report = '报告期限'
    simple = '按季度'
    year = '按年度'
