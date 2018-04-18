#!/usr/bin/python
# -*- coding: UTF-8 -*-
import src.base.read_data.read_xls as read_xls
import src.base.constans.Cash as cash

if __name__ =='__main__':
    files = read_xls.readFiles("/Users/fanpu/developer/资金/苏宁易购")
    print(cash.Cash.absorbInvestAmount)