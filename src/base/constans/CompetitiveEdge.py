# -*- coding: UTF-8 -*-

from enum import Enum

class CompetitiveEdge(Enum):
    # 评估历史盈利能力
    HistoricalProfitability = 'HistoricalProfitability'
    # 评估利润来源
    SourceOfProfits = 'SourceOfProfits'
    # 评估竞争优势周期
    EvaluateCompetitiveAdvantageCycle = 'EvaluateCompetitiveAdvantageCycle'
    # 分析行业结构
    AnalysisIndustryStructure = 'AnalysisIndustryStructure'
    # 分析自由现金流的组成