# -*- coding: UTF-8 -*-

from enum import Enum

# 主要指标
class Main(Enum):
    BasicEarningsPerShare = '基本每股收益(元)'
    RetainedProfits = '净利润(元)'
    RetainedProfitsGrowth= '净利润同比增长率()'
    NonNetRetainedProfits = '扣非净利润(元)'
    NonNetRetainedProfitsGrowth= '扣非净利润同比增长率()'
    GrossRevenue = '营业总收入(元)'
    GrossRevenueGrowth = '营业总收入同比增长率()'
    NetAssetsPerShare= '每股净资产(元)'
    ReturnOnEquity = '净资产收益率()'
    ReturnOnEquityDilution= '净资产收益率-摊薄()'
    RatioAssetsLiabilities= '资产负债比率()'
    CapitalReservePerShare = '每股资本公积金(元)'
    UndistributedProfitPerShare = '每股未分配利润(元)'
    OperatingCashFlowPerShare = '每股经营现金流(元)'
    GrossProfitRate = '销售毛利率()'
    InventoryTurnover = '存货周转率()'
    NetProfitMarginOnSales = '销售净利率()'