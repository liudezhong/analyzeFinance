# -*- coding: UTF-8 -*-

import src.base.commons.commonUtils as commonUtils
import src.base.constans.Benefit as benefitEnum
import src.base.constans.Debt as debtEnum
import src.base.constans.Cash as cashEnum
import src.base.constans.Main as mainEnum
import src.base.constans.Pay as payEnum

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
    totalAssetsTurnover = commonUtils.handleDivisionZero(operationRevenue, totalAssets)
    print('计算总资产周转率结果为: ', totalAssetsTurnover),
    return totalAssetsTurnover


# 计算销售净利率 = 净利润/营业总收入 净利润=利润总额-所得税
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
    netProfitMarginOnSales = commonUtils.handleDivisionZero(retainedProfits, grossRevenue)
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
    equityMultiplier = commonUtils.handleDivisionZero(totalAssets, totalShareHolderSequity)
    print('计算权益乘数结果为：', equityMultiplier)
    return equityMultiplier

# 计算资产负债率 = 负债总额/资产总额
def calAssetLiabilityRatio(subject, data):
    # 计算负债总额
    totalLiabilities = calTotalLiabilities(subject, data)
    # 资产总额
    totalAssets = calTotalAssets(subject, data)
    # 计算资产率
    assetLiabilityRatio = commonUtils.handleDivisionZero(totalLiabilities, totalAssets)
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

#计算自由现金流 = 经营性现金流（经营现金流量净额） - 资本支出（购建固定资产和其他支付的现金）
def calFreeCashFlow(subject, data):
    # 计算经营性现金流（经营现金流量净额）
    busiAmount = commonUtils.calCommonIndex(subject, data, cashEnum.Cash.BusiAmount.value)
    # 计算资本支出（购建固定资产和其他支付的现金）
    buildFixedAssetsAmount = commonUtils.calCommonIndex(subject, data, cashEnum.Cash.BuildFixedAssetsAmount.value)
    freeCashFlow = busiAmount - buildFixedAssetsAmount
    print('计算自由现金流结果为：', freeCashFlow)
    return freeCashFlow

# 计算资产收益率 = 净收益（净利润）/公司全部资产
def calReturnOnAssets(benefitSubject, benefitData, debtSubject, debtData):
    # 计算净利润
    retainedProfits = calRetainedProfits(benefitSubject, benefitData)
    # 计算公司全部资产
    totalAssets = calTotalAssets(debtSubject, debtData)
    returnOnAssets = commonUtils.handleDivisionZero(retainedProfits, totalAssets)
    print('计算资产收益率的结果为：', returnOnAssets)
    return returnOnAssets

# 计算毛利率
def calGrossProfitRate(subject, data):
    return commonUtils.calCommonIndex(subject, data, mainEnum.Main.GrossProfitRate.value)

# 计算经营性现金流（经营现金流量净额）
def calbusiAmount(subject, data):
    return commonUtils.calCommonIndex(subject, data, cashEnum.Cash.BusiAmount.value)

# 计算资本支出（购建固定资产和其他支付的现金）
def calBuildFixedAssetsAmount(subject, data):
    return commonUtils.calCommonIndex(subject, data, cashEnum.Cash.BuildFixedAssetsAmount.value)

# 计算 销售商品、提供劳务收到的现金(元)（销售收入）
def calSellProvAmount(subject, data):
    return commonUtils.calCommonIndex(subject, data, cashEnum.Cash.SellProvAmount.value)

# 计算自由现金流对销售收入的比率
def calFreeCashFlowDivideSell(subject, data):
    # 计算自由现金流
    freeCashFlow = calFreeCashFlow(subject, data)
    # 销售商品、提供劳务收到的现金(元)（销售收入）
    sellProvAmount = calSellProvAmount(subject, data)
    # 计算自由现金流对销售收入的比率
    freeCashFlowDivideSell = commonUtils.handleDivisionZero(freeCashFlow, sellProvAmount)
    print('计算自由现金流对销售收入的比率: ', freeCashFlowDivideSell)
    return freeCashFlowDivideSell

# 计算营业利润
def calOperatingProfit(subject, data):
    return commonUtils.calCommonIndex(subject, data, benefitEnum.Benefit.OperatingProfit.value)

# 计算营业毛利率
def calOperatingMargin(subject, data):
    # 计算营业收入
    operationRevenue = commonUtils.calCommonIndex(subject, data, benefitEnum.Benefit.OperationRevenue.value)
    # 计算营业成本
    operatingCost = calOperatingCost(subject, data)
    # 计算营业毛利率
    operatingMargin = commonUtils.handleDivisionZero((operationRevenue - operatingCost), operationRevenue)
    print('计算营业毛利率的结果为：', operatingMargin)
    return operatingMargin

# 计算负债权益比率=负债总额/所有者权益总额
def calDebtEquityRatio(subject, data):
    # 计算负债总额
    totalLiabilities = calTotalLiabilities(subject, data)
    # 计算所有者权益总额
    totalShareHolderSequity = calTotalShareHolderSequity(subject, data)
    # 计算负债权益比率
    debtEquityRatio = commonUtils.handleDivisionZero(totalLiabilities, totalShareHolderSequity)
    print('计算负债权益比率结果是：', debtEquityRatio)
    return debtEquityRatio

# 计算扣非净利润(元)
def calTakeNonRetainedProfits(subject, data):
    return commonUtils.calCommonIndex(subject, data, benefitEnum.Benefit.TakeNonRetainedProfits.value)

# 计算净利润同比增长率()
def calRetainedProfitsGrowth(subject, data):
    return commonUtils.calCommonIndex(subject, data, mainEnum.Main.RetainedProfitsGrowth.value)

# 计算扣非净利润同比增长率()
def calNonNetRetainedProfitsGrowth(subject, data):
    return commonUtils.calCommonIndex(subject, data, mainEnum.Main.NonNetRetainedProfitsGrowth.value)
# 计算营业收入
def calOperationRevenue(subject, data):
    return commonUtils.calCommonIndex(subject, data, benefitEnum.Benefit.OperationRevenue.value)
# 计算流动比率()
def calCurrentRatio(subject, data):
    return commonUtils.calCommonIndex(subject, data, payEnum.Pay.CurrentRatio.value)
# 计算速动比率
def calQuickRatio(subject, data):
    return commonUtils.calCommonIndex(subject, data, payEnum.Pay.QuickRatio.value)
# 计算保守速动比率
def calConserQuickRatio(subject, data):
    return commonUtils.calCommonIndex(subject, data, payEnum.Pay.ConserQuickRatio.value)
