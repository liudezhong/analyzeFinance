# -*- coding: UTF-8 -*-

from enum import Enum

# 利润表常量
class Benefit(Enum):
    RetainedProfits = '净利润(元)'
    TakeNonRetainedProfits = '扣非净利润(元)'
    GrossRevenue = '营业总收入(元)'
    OperationRevenue = '营业收入(元)'
    TotalOperatingCost = '营业总成本(元)'
    OperatingCost = '营业成本(元)'
    OperatingProfit = '营业利润(元)'
    IncomeFromInvestment = '投资收益(元)'
    UnionIncomeFromInvestment = '其中：联营企业和合营企业的投资收益(元)'
    LossFromAssetDevaluation = '资产减值损失(元)'
    AdministrationExpense = '管理费用(元)'
    SelledExpense = '销售费用(元)'
    FinanceExpense = '财务费用(元)'
    NonbusinessIncome = '营业外收入(元)'
    NonbusinessExpenditure = '营业外支出(元)'
    BusinessTaxAndSurcharges = '营业税金及附加(元)'
    TotalProfit = '利润总额(元)'
    IncomeTax = '所得税(元)'
    OtherComprehensiveIncome = '其他综合收益(元)'
    TotalComprehensiveIncome = '综合收益总额(元)'
    ParentComTotalComprehensiveIncome = '归属于母公司股东的综合收益总额(元)'
    MinorityTotalComprehensiveIncome = '归属于少数股东的综合收益总额(元)'