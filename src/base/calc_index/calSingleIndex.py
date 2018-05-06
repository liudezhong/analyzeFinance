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
    print(' 计算其他利润结果为: ',  otherOperatingProfit),
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
    return commonUtils.calCommonIndex(subject, data, debtEnum.Debt.TotalCurrentLiabilities.value);

# 计算总资产周转率 = 营业收入/资产总计
def calTotalAssetsTurnover(benefitSubject, benefitData, debtSubject, debtData):
    operationRevenue = commonUtils.calCommonIndex(benefitSubject, benefitData, benefitEnum.Benefit.OperationRevenue.value)
    totalAssets = commonUtils.calCommonIndex(debtSubject, debtData, debtEnum.Debt.TotalAssets.value)
    totalAssetsTurnover = operationRevenue/totalAssets
    print('计算总资产周转率结果为: ', totalAssetsTurnover),
    return totalAssetsTurnover

# todo 计算销售净利润
def calNetProfitMarginOnSales(data):
    pass

# todo 计算所有者权益总额
def calOwnershipInterestCount(data):
    pass

# 计算资产总额
def calTotalAssets(subject, data):
    return commonUtils.calCommonIndex(subject, data, debtEnum.Debt.TotalAssets.value)

# 计算负债总额
def calTotalLiabilities(subject, data):
    return commonUtils.calCommonIndex(subject, data, debtEnum.Debt.TotalLiability.value)

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
