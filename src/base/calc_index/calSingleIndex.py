# -*- coding: UTF-8 -*-

import src.base.constans.Benefit as benefitEnum
import src.base.constans.Debt as debtEnum
import src.base.constans.Export as exportEnum

import src.base.commons.commonUtils as commonUtils


# 计算财务费用
def calFinanceExpense(data):
    return commonUtils.calCommonIndex(data, benefitEnum.Benefit.FinanceExpense.name)

# 计算管理费用
def calAdministrationExpense(data):
    return commonUtils.calCommonIndex(data, benefitEnum.Benefit.AdministrationExpense.name)

# 计算销售费用
def calSelledExpense(data):
    return commonUtils.calCommonIndex(data, benefitEnum.Benefit.SelledExpense.name)

# 计算营业成本
def calOperatingCost(data):
    return commonUtils.calCommonIndex(data, benefitEnum.Benefit.OperatingCost)

# 计算所得税
def calIncomeTax(data):
    return commonUtils.calCommonIndex(data, benefitEnum.Benefit.IncomeTax)

# todo 计算其他利润 公式为 营业外收入 - 营业外支出
def calOtherOperatingProfit(data):
    pass

# 计算总成本
def calTotalOperatingCost(data):
    return commonUtils.calCommonIndex(data, benefitEnum.Benefit.TotalOperatingCost)

# 计算营业总收入
def calGrossRevenue(data):
    return commonUtils.calCommonIndex(data, benefitEnum.Benefit.GrossRevenue)

# 计算存货
def calStock(data):
    return commonUtils.calCommonIndex(data, debtEnum.Debt.Stock);

# 计算应收账款
def calReceiveCredit(data):
    return commonUtils.calCommonIndex(data, debtEnum.Debt.ReceiveCredit)

# 计算货币资金
def calCurrencyMoney(data):
    return commonUtils.calCommonIndex(data, debtEnum.Debt.CurrencyMoney)

# 计算净利润
def calRetainedProfits(data):
    return commonUtils.calCommonIndex(data, benefitEnum.Benefit.RetainedProfits)

# 计算非流动资产
def calTotalNoncurrentAssets(data):
    return commonUtils.calCommonIndex(data, debtEnum.Debt.TotalNoncurrentAssets)

# 计算流动资产
def calFlowAssetCount(data):
    return commonUtils.calCommonIndex(data, debtEnum.Debt.FlowAssetCount)

# 计算非流动负债
def calTotalNoncurrentLiabilities(data):
    return commonUtils.calCommonIndex(data, debtEnum.Debt.TotalNoncurrentLiabilities)

# 计算流动负债
def calTotalCurrentLiabilities(data):
    return commonUtils.calCommonIndex(data, debtEnum.Debt.TotalCurrentLiabilities);

# todo 计算总资产周转率
def calTotalAssetsTurnover(data):
    pass

# todo 计算销售净利润
def calNetProfitMarginOnSales(data):
    pass

# todo 计算所有者权益总额
def calOwnershipInterestCount(data):
    pass

# 计算资产总额
def calTotalAssets(data):
    return commonUtils.calCommonIndex(data, debtEnum.Debt.TotalAssets)

# 计算负债总额
def calTotalLiabilities(data):
    return commonUtils.calCommonIndex(data, debtEnum.Debt.TotalLiability)

# todo 计算总资产收益率
def calReturnOnTotalAssets(data):
    pass

# todo 计算权益乘数
def calEquityMultiplier(data):
    pass

# todo 计算资产负债率
def calAssetLiabilityRatio(data):
    pass

# 计算净资产收益率
def calReturnOnEquity(data):
    pass
