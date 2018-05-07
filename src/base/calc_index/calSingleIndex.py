# -*- coding: UTF-8 -*-

import src.base.commons.commonUtils as commonUtils
import src.base.constans.Benefit as benefitEnum
import src.base.constans.Debt as debtEnum


# 计算财务费用
def calFinanceExpense(subject, data):
    return commonUtils.calCommonIndex(subject, data, benefitEnum.Benefit.FinanceExpense.value)


# 计算管理费用
def calAdministrationExpense(subject, data):
    return commonUtils.calCommonIndex(subject, data, benefitEnum.Benefit.AdministrationExpense.value)


# 计算销售费用
def calSelledExpense(subject, data):
    return commonUtils.calCommonIndex(subject, data, benefitEnum.Benefit.SelledExpense.value)


# 计算营业成本
def calOperatingCost(subject, data):
    return commonUtils.calCommonIndex(subject, data, benefitEnum.Benefit.OperatingCost.value)


# 计算所得税
def calIncomeTax(subject, data):
    return commonUtils.calCommonIndex(subject, data, benefitEnum.Benefit.IncomeTax.value)


# 计算其他利润 = 营业外收入 - 营业外支出
def calOtherOperatingProfit(subject, data):
    nonbusinessIncome = commonUtils.calCommonIndex(subject, data, benefitEnum.Benefit.NonbusinessIncome.value)
    nonbusinessExpenditure = commonUtils.calCommonIndex(subject, data, benefitEnum.Benefit.NonbusinessExpenditure.value)
    otherOperatingProfit = nonbusinessIncome - nonbusinessExpenditure
    print(' 计算其他利润结果为: ', otherOperatingProfit),
    return otherOperatingProfit


# 计算总成本
def calTotalOperatingCost(subject, data):
    return commonUtils.calCommonIndex(subject, data, benefitEnum.Benefit.TotalOperatingCost.value)


# 计算营业总收入
def calGrossRevenue(subject, data):
    return commonUtils.calCommonIndex(subject, data, benefitEnum.Benefit.GrossRevenue.value)


# 计算存货
def calStock(subject, data):
    return commonUtils.calCommonIndex(subject, data, debtEnum.Debt.Stock.value);


# 计算应收账款
def calReceiveCredit(subject, data):
    return commonUtils.calCommonIndex(subject, data, debtEnum.Debt.ReceiveCredit.value)


# 计算货币资金
def calCurrencyMoney(subject, data):
    return commonUtils.calCommonIndex(subject, data, debtEnum.Debt.CurrencyMoney.value)


# 计算净利润
def calRetainedProfits(subject, data):
    return commonUtils.calCommonIndex(subject, data, benefitEnum.Benefit.RetainedProfits.value)


# 计算非流动资产
def calTotalNoncurrentAssets(subject, data):
    return commonUtils.calCommonIndex(subject, data, debtEnum.Debt.TotalNoncurrentAssets.value)


# 计算流动资产
def calFlowAssetCount(subject, data):
    return commonUtils.calCommonIndex(subject, data, debtEnum.Debt.FlowAssetCount.value)


# 计算非流动负债
def calTotalNoncurrentLiabilities(subject, data):
    return commonUtils.calCommonIndex(subject, data, debtEnum.Debt.TotalNoncurrentLiabilities.value)


# 计算流动负债
def calTotalCurrentLiabilities(subject, data):
    return commonUtils.calCommonIndex(subject, data, debtEnum.Debt.TotalCurrentLiabilities.value)


# 计算总资产周转率 = 营业收入/资产总计
def calTotalAssetsTurnover(benefitSubject, benefitData, debtSubject, debtData):
    operationRevenue = commonUtils.calCommonIndex(benefitSubject, benefitData,
                                                  benefitEnum.Benefit.OperationRevenue.value)
    totalAssets = commonUtils.calCommonIndex(debtSubject, debtData, debtEnum.Debt.TotalAssets.value)
    totalAssetsTurnover = operationRevenue / totalAssets
    print('计算总资产周转率结果为: ', totalAssetsTurnover),
    return totalAssetsTurnover


# todo 计算销售净利率 = 净利润/营业总收入 净利润=利润总额-所得税
def calNetProfitMarginOnSales(benefitSubject, benefitData):
    # 利润总额
    totalProfit = commonUtils.calCommonIndex(benefitSubject, benefitData, benefitEnum.Benefit.TotalProfit.value)
    # 所得税
    incomeTax = commonUtils.calCommonIndex(benefitSubject, benefitData, benefitEnum.Benefit.IncomeTax.value);
    # 净利润
    retainedProfits = totalProfit - incomeTax
    print('净利润=利润总额-所得税 = ', retainedProfits),
    # 营业总收入
    grossRevenue = commonUtils.calCommonIndex(benefitSubject, benefitData, benefitEnum.Benefit.GrossRevenue.value)
    # 销售净利润
    netProfitMarginOnSales = retainedProfits / grossRevenue
    print('计算销售净利率结果为: ', netProfitMarginOnSales),
    return netProfitMarginOnSales

# 计算资产总额
def calTotalAssets(subject, data):
    return commonUtils.calCommonIndex(subject, data, debtEnum.Debt.TotalAssets.value)


# 计算负债总额
def calTotalLiabilities(subject, data):
    return commonUtils.calCommonIndex(subject, data, debtEnum.Debt.TotalLiability.value)


# 计算总资产收益率 = 销售净利率 * 总资产周转率
def calReturnOnTotalAssets(benefitSubject, benefitData, debtSubject, debtData):
    # 计算销售净利率
    netProfitMarginOnSales = calNetProfitMarginOnSales(benefitSubject, benefitData)
    print('计算总资产收益率 - 销售净利率', netProfitMarginOnSales)
    # 计算总资产周转率
    totalAssetsTurnover = calTotalAssetsTurnover(benefitSubject, benefitData, debtSubject, debtData)
    print('计算总资产收益率 - 总资产周转率', totalAssetsTurnover)
    returnOnTotalAssets = netProfitMarginOnSales * totalAssetsTurnover
    print('计算总资产收益率结果为：', returnOnTotalAssets)
    return returnOnTotalAssets

# 计算权益乘数 = 资产总额 / 所有者权益总额（股东权益合计）
def calEquityMultiplier(subject, data):
    # 计算资产总额
    totalAssets = calTotalAssets(subject, data)
    # 计算所有者权益总额
    totalShareHolderSequity = calTotalShareHolderSequity(subject, data)
    # 计算权益乘数
    equityMultiplier = totalAssets/totalShareHolderSequity
    print('计算权益乘数结果为：', equityMultiplier)
    return equityMultiplier

# 计算资产负债率 = 负债总额/资产总额
def calAssetLiabilityRatio(subject, data):
    # 计算负债总额
    totalLiabilities = calTotalLiabilities(subject, data)
    # 资产总额
    totalAssets = calTotalAssets(subject, data)
    # 计算资产率
    assetLiabilityRatio = totalLiabilities/totalAssets
    print('计算资产负债率结果为：', assetLiabilityRatio),
    return assetLiabilityRatio

# 计算净资产收益率 = 权益乘数 * 总资产收益率
def calReturnOnEquity(benefitSubject, benefitData, debtSubject, debtData):
    # 计算权益乘数
    equityMultiplier = calEquityMultiplier(debtSubject, debtData)
    print('计算净资产收益率 - 权益乘数结果为', equityMultiplier),
    # 计算总资产收益率
    returnOnTotalAssets = calReturnOnTotalAssets(benefitSubject, benefitData, debtSubject, debtData)
    # 计算净资产收益率
    returnOnEquity = equityMultiplier * returnOnTotalAssets
    print('计算净资产收益率结果为：', returnOnEquity)
    return returnOnEquity

# 计算股东权益合计
def calTotalShareHolderSequity(subject, data):
    return commonUtils.calCommonIndex(subject, data, debtEnum.Debt.TotalShareHolderSequity.value)