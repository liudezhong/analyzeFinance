# -*- coding: UTF-8 -*-

from enum import Enum

# 主要指标
class Pay(Enum):
    CurrentRatio = '流动比率()'
    QuickRatio = '速动比率()'
    ConserQuickRatio = '保守速动比率()'
