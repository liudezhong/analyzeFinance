# -*- coding: UTF-8 -*-

from enum import Enum

# 计算的常用指标
class CalcIndex(Enum):
    FinanceExpense = '财务费用'
    AdministrationExpense = '管理费用'
    SelledExpense = '销售费用'
    OperatingCost = '营业成本'
    IncomeTax = '所得税'
    OtherOperatingProfit = '其他利润'
    TotalOperatingCost = '总成本'
    GrossRevenue = '营业总收入'
    Stock = '存货'
    ReceiveCredit = '应收账款'
    CurrencyMoney = '货币资金'
    RetainedProfits = '净利润'
    TotalNoncurrentAssets = '非流动资产'
    FlowAssetCount = '流动资产'
    TotalNoncurrentLiabilities = '非流动负债'
    TotalCurrentLiabilities = '流动负债'
    TotalAssetsTurnover = '总资产周转率'
    NetProfitMarginOnSales = '销售净利率'
    OwnershipInterestCount = '所有者权益总额' # 股东权益合计
    TotalAssets = '资产总额'
    TotalLiabilities = '负债总额'
    ReturnOnTotalAssets = '总资产收益率'
    EquityMultiplier = '权益乘数'
    AssetLiabilityRatio = '资产负债率'
    ReturnOnEquity = '净资产收益率'
    FreeCashFlow = '自由现金流'
    ReturnOnAssets = '资产收益率'
    GrossProfitRate = '毛利率'
    BusiAmount = '经营现金流量净额'
    BuildFixedAssetsAmount = '购建固定资产和其他支付的现金' #资本支出
    SellProvAmount = '销售商品、提供劳务收到的现金(元)'
    FreeCashFlowDivideSell = '自由现金流/销售收入'
    OperatingProfit = '营业利润'
    OperatingMargin = '营业毛利率'
    DebtEquityRatio = '负债权益比率'
    TakeNonRetainedProfits = '扣非净利润(元)'
    RetainedProfitsGrowth= '净利润同比增长率()'
    NonNetRetainedProfitsGrowth= '扣非净利润同比增长率()'
