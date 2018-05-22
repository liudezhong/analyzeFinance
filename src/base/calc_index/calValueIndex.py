# -*- coding: UTF-8 -*-
import src.base.commons.commonUtils as commUtils
import src.base.obtain_data.obtainData as obtainUtils
import src.base.constans.Netease as netEnum

# 计算流通A股(亿股)
def calCirculateCount(code):
    gdfxInfo = obtainUtils.obtainHtmlFromNetease(code, netEnum.Netease.gdfx.value)
    circulateCount = commUtils.getCirculateCount(gdfxInfo)
    print('计算流通A股总数的结果为：', circulateCount)
    return {'circulateCount': circulateCount}




