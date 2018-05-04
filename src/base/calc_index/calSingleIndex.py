# -*- coding: UTF-8 -*-

import src.base.constans.Benefit as benefitEnum
import src.base.constans.Export as exportEnum

# 计算财务费用
def calFinanceExpense(data):
    result = 0
    index = 0
    trigger = False
    for name, member in benefitEnum.Benefit.__members__.items():
        if (name == benefitEnum.Benefit.FinanceExpense.name):
            trigger = True
            break
        index += 1
    if trigger:
        result = data[index]
    else:
        result = None
    print('计算财务费用完成, 结果为：', result)
    return result;

