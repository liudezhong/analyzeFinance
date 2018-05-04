# -*- coding: UTF-8 -*-

from enum import Enum

# 现金流量表常量
class Cash(Enum):
    SellProvAmount = '销售商品、提供劳务收到的现金(元)'
    RecFeeReturnAmount = '收到的税费与返还(元)'
    PayVariousFeeAmount = '支付的各项税费(元)'
    PayEmployeeAmount = '支付给职工以及为职工支付的现金(元)'
    BusiIntoAmount = '经营现金流入(元)'
    BusiOutAmount = '经营现金流出(元)'
    BusiAmount = '经营现金流量净额(元)'
    ProcessFixInvisibleAmount = '处置固定资产、无形资产的现金(元)'
    ProcessSonOtherAmount = '处置子公司及其他收到的现金(元)'
    BuildFixedAssetsAmount = '购建固定资产和其他支付的现金(元)'
    InvestPayAmount = '投资支付的现金(元)'
    GetSonCAmount = '取得子公司现金净额(元)'
    InvestIntoAmount = '投资现金流入(元)'
    InvestOutAmount = '投资现金流出(元)'
    InvestAmount = '投资现金流量净额(元)'
    absorbInvestAmount = '吸收投资收到现金(元)'
    SonCAbsorbInvestAmount = '其中子公司吸收现金(元)'
    AcquireBorrowAmount = '取得借款的现金(元)'
    GetOtherFinancingAmount = '收到其他与筹资的现金(元)'
    RepayDebtCashAmount = '偿还债务支付现金(元)'
    DistDividendsProfitAmount = '分配股利、利润或偿付利息支付的现金(元)'
    SonCDistDividendsProfitAmount = '其中子公司支付股利(元)'
    PayOtherFinancingAmount = '支付其他与筹资的现金(元)'
    FinancingIntoAmount = '筹资现金流入(元)'
    FinancingOutAmount = '筹资现金流出(元)'
    FinancingAmount = '筹资现金流量净额(元)'
    ExchangeRateAmount = '汇率变动对现金的影响(元)'
    CashEquivalentAddMount = '现金及现金等价物净增加额(元)'