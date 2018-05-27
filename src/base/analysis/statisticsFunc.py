# -*- coding: UTF-8 -*-
import pandas as pd
import src.base.commons.CommonUtils as commUtils
import src.base.constans.Analysis as analysisEnum
import src.base.constans.Finance as financeEnum
import src.base.handle_data.handleIndexToExcel as handleUtils
import src.base.constans.CalcIndex as calcIndexEnum
from matplotlib.font_manager import _rebuild
_rebuild()  # reload一下

# 多个数据单独显示统计公共方法
def statisticsMultiBaseFunc(code, sliceList, assessmentItem):
    for name, member in financeEnum.Finance.__members__.items():
        # 展示自由现金流 1、按照报告周期 2、季度 3、年
        analyzeTableFileName = commUtils.getAnalysisFilePath(analysisEnum.Analysis.analysis.value, name, code)
        df = pd.read_excel(analyzeTableFileName, sheet_name=analysisEnum.Analysis.analysis.value, header=0)
        print('周期为：', name, '计算', assessmentItem, '开始')
        enumList = commUtils.historicalProfitabilityEnumIndex(sliceList)
        handleUtils.handleSpecialIndexToExcel(df, enumList, analysisEnum.Analysis.analysis.value, name, code,
                                              assessmentItem)
        print('周期为：', name, '计算', assessmentItem, '结束 绘图开始')
        commUtils.multiShowPlot(df, enumList, analysisEnum.Analysis.analysis.value, name, code, assessmentItem)
        print('周期为：', name, assessmentItem, '，绘图结束')

# 多个数据显示在一张图上
def statisticsSingleBaseFunc(code, sliceList, assessmentItem):
    for name, member in financeEnum.Finance.__members__.items():
        # 展示自由现金流 1、按照报告周期 2、季度 3、年
        analyzeTableFileName = commUtils.getAnalysisFilePath(analysisEnum.Analysis.analysis.value, name, code)
        df = pd.read_excel(analyzeTableFileName, sheet_name=analysisEnum.Analysis.analysis.value, header=0)
        print('周期为：', name, '计算', assessmentItem, '开始')
        enumList = commUtils.historicalProfitabilityEnumIndex(sliceList)
        handleUtils.handleSpecialIndexToExcel(df, enumList, analysisEnum.Analysis.analysis.value, name, code, assessmentItem)
        print('周期为：', name, '计算', assessmentItem, '结束 绘图开始')
        commUtils.singleShowPlot(df, enumList, analysisEnum.Analysis.analysis.value, name, code, assessmentItem)
        print('周期为：', name, assessmentItem, '，绘图结束')

# 获取需要展示的分析数据项
def historicalProfitabilityEnumIndex(dataList):
    indexList = []
    for data in dataList:
        count = 0
        for name, member in calcIndexEnum.CalcIndex.__members__.items():
            if data == member.value:
                indexList.append(count)
                break
            count += 1
    return indexList