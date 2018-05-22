# -*- coding: UTF-8 -*-

import copy
import datetime
import os
import platform

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.font_manager import _rebuild

import src.base.constans.CalcIndex as calcIndexEnum
import src.base.constans.Constans as constansEnum
import src.base.constans.File as fileEnum
import src.base.constans.OSSystem as osEnum
import src.base.constans.Type as typeEnum
import src.base.constans.Netease as netEnum
from bs4 import BeautifulSoup

_rebuild()  # reload一下

cellList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN',
            'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ', 'BA', 'BB', 'BC', 'BD', 'BE', 'BF',
            'BG', 'BH', 'BI', 'BJ', 'BK', 'BL', 'BM', 'BN', 'BO', 'BP', 'BQ', 'BR', 'BS', 'BT', 'BU', 'BV', 'BW', 'BX',
            'BY', 'BZ', 'CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG', 'CH', 'CI', 'CJ', 'CK', 'CL', 'CM', 'CN', 'CO', 'CP',
            'CQ', 'CR', 'CS', 'CT', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DA', 'DB', 'DC', 'DD', 'DE', 'DF', 'DG', 'DH',
            'DI', 'DJ', 'DK', 'DL', 'DM', 'DN', 'DO', 'DP', 'DQ', 'DR', 'DS', 'DT', 'DU', 'DV', 'DW', 'DX', 'DY', 'DZ',
            'EA', 'EB', 'EC', 'ED', 'EE', 'EF', 'EG', 'EH', 'EI', 'EJ', 'EK', 'EL', 'EM', 'EN', 'EO', 'EP', 'EQ', 'ER',
            'ES', 'ET', 'EU', 'EV', 'EW', 'EX', 'EY', 'EZ', 'FA', 'FB', 'FC', 'FD', 'FE', 'FF', 'FG', 'FH', 'FI', 'FJ',
            'FK', 'FL', 'FM', 'FN', 'FO', 'FP', 'FQ', 'FR', 'FS', 'FT', 'FU', 'FV', 'FW', 'FX', 'FY', 'FZ', 'GA', 'GB',
            'GC', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GJ', 'GK', 'GL', 'GM', 'GN', 'GO', 'GP', 'GQ', 'GR', 'GS', 'GT',
            'GU', 'GV', 'GW', 'GX', 'GY', 'GZ', 'HA', 'HB', 'HC', 'HD', 'HE', 'HF', 'HG', 'HH', 'HI', 'HJ', 'HK', 'HL',
            'HM', 'HN', 'HO', 'HP', 'HQ', 'HR', 'HS', 'HT', 'HU', 'HV', 'HW', 'HX', 'HY', 'HZ', 'IA', 'IB', 'IC', 'ID',
            'IE', 'IF', 'IG', 'IH', 'II', 'IJ', 'IK', 'IL', 'IM', 'IN', 'IO', 'IP', 'IQ', 'IR', 'IS', 'IT', 'IU', 'IV',
            'IW', 'IX', 'IY', 'IZ', 'JA', 'JB', 'JC', 'JD', 'JE', 'JF', 'JG', 'JH', 'JI', 'JJ', 'JK', 'JL', 'JM', 'JN',
            'JO', 'JP', 'JQ', 'JR', 'JS', 'JT', 'JU', 'JV', 'JW', 'JX', 'JY', 'JZ', 'KA', 'KB', 'KC', 'KD', 'KE', 'KF',
            'KG', 'KH', 'KI', 'KJ', 'KK', 'KL', 'KM', 'KN', 'KO', 'KP', 'KQ', 'KR', 'KS', 'KT', 'KU', 'KV', 'KW', 'KX',
            'KY', 'KZ', 'LA', 'LB', 'LC', 'LD', 'LE', 'LF', 'LG', 'LH', 'LI', 'LJ', 'LK', 'LL', 'LM', 'LN', 'LO', 'LP',
            'LQ', 'LR', 'LS', 'LT', 'LU', 'LV', 'LW', 'LX', 'LY', 'LZ', 'MA', 'MB', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH',
            'MI', 'MJ', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ',
            'NA', 'NB', 'NC', 'ND', 'NE', 'NF', 'NG', 'NH', 'NI', 'NJ', 'NK', 'NL', 'NM', 'NN', 'NO', 'NP', 'NQ', 'NR',
            'NS', 'NT', 'NU', 'NV', 'NW', 'NX', 'NY', 'NZ', 'OA', 'OB', 'OC', 'OD', 'OE', 'OF', 'OG', 'OH', 'OI', 'OJ',
            'OK', 'OL', 'OM', 'ON', 'OO', 'OP', 'OQ', 'OR', 'OS', 'OT', 'OU', 'OV', 'OW', 'OX', 'OY', 'OZ', 'PA', 'PB',
            'PC', 'PD', 'PE', 'PF', 'PG', 'PH', 'PI', 'PJ', 'PK', 'PL', 'PM', 'PN', 'PO', 'PP', 'PQ', 'PR', 'PS', 'PT',
            'PU', 'PV', 'PW', 'PX', 'PY', 'PZ', 'QA', 'QB', 'QC', 'QD', 'QE', 'QF', 'QG', 'QH', 'QI', 'QJ', 'QK', 'QL',
            'QM', 'QN', 'QO', 'QP', 'QQ', 'QR', 'QS', 'QT', 'QU', 'QV', 'QW', 'QX', 'QY', 'QZ', 'RA', 'RB', 'RC', 'RD',
            'RE', 'RF', 'RG', 'RH', 'RI', 'RJ', 'RK', 'RL', 'RM', 'RN', 'RO', 'RP', 'RQ', 'RR', 'RS', 'RT', 'RU', 'RV',
            'RW', 'RX', 'RY', 'RZ', 'SA', 'SB', 'SC', 'SD', 'SE', 'SF', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN',
            'SO', 'SP', 'SQ', 'SR', 'SS', 'ST', 'SU', 'SV', 'SW', 'SX', 'SY', 'SZ', 'TA', 'TB', 'TC', 'TD', 'TE', 'TF',
            'TG', 'TH', 'TI', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TP', 'TQ', 'TR', 'TS', 'TT', 'TU', 'TV', 'TW', 'TX',
            'TY', 'TZ', 'UA', 'UB', 'UC', 'UD', 'UE', 'UF', 'UG', 'UH', 'UI', 'UJ', 'UK', 'UL', 'UM', 'UN', 'UO', 'UP',
            'UQ', 'UR', 'US', 'UT', 'UU', 'UV', 'UW', 'UX', 'UY', 'UZ', 'VA', 'VB', 'VC', 'VD', 'VE', 'VF', 'VG', 'VH',
            'VI', 'VJ', 'VK', 'VL', 'VM', 'VN', 'VO', 'VP', 'VQ', 'VR', 'VS', 'VT', 'VU', 'VV', 'VW', 'VX', 'VY', 'VZ',
            'WA', 'WB', 'WC', 'WD', 'WE', 'WF', 'WG', 'WH', 'WI', 'WJ', 'WK', 'WL', 'WM', 'WN', 'WO', 'WP', 'WQ', 'WR',
            'WS', 'WT', 'WU', 'WV', 'WW', 'WX', 'WY', 'WZ', 'XA', 'XB', 'XC', 'XD', 'XE', 'XF', 'XG', 'XH', 'XI', 'XJ',
            'XK', 'XL', 'XM', 'XN', 'XO', 'XP', 'XQ', 'XR', 'XS', 'XT', 'XU', 'XV', 'XW', 'XX', 'XY', 'XZ', 'YA', 'YB',
            'YC', 'YD', 'YE', 'YF', 'YG', 'YH', 'YI', 'YJ', 'YK', 'YL', 'YM', 'YN', 'YO', 'YP', 'YQ', 'YR', 'YS', 'YT',
            'YU', 'YV', 'YW', 'YX', 'YY', 'YZ', 'ZA', 'ZB', 'ZC', 'ZD', 'ZE', 'ZF', 'ZG', 'ZH', 'ZI', 'ZJ', 'ZK', 'ZL',
            'ZM', 'ZN', 'ZO', 'ZP', 'ZQ', 'ZR', 'ZS', 'ZT', 'ZU', 'ZV', 'ZW', 'ZX', 'ZY', 'ZZ']


# 创建目录
def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径


# 判断操作系统
def judgeOs():
    sysOs = platform.system()
    if (sysOs == "Windows"):
        return 'Windows'
    elif (sysOs == "Linux"):
        return 'Linux'
    else:
        return 'Other'


# 获取基本文件目录
def getBaseFileDir(os):
    if (os == osEnum.OSSystem.Windows.value):
        return fileEnum.File.WindowsFinanceFile.value
    elif (os == osEnum.OSSystem.Linux.value):
        return fileEnum.File.LinuxFinanceFile.value
    else:
        return fileEnum.File.OtherFinanceFile.value


# 获取不同操作系统之间的连接符
def getSymbleByOs(os):
    if (os == osEnum.OSSystem.Windows.value):
        return "\\"
    elif (os == osEnum.OSSystem.Linux.value):
        return "/"
    else:
        return "/"


# 获取当前文件路径
def getCurrentFilePath(export, type, code, original):
    os = judgeOs()
    basePath = getBaseFileDir(os)
    symble = getSymbleByOs(os)
    fileType = typeEnum.Type.original.value if type == None else type
    basePathName = basePath + code + symble + fileType + symble + export + symble + export
    filePathName = basePathName + '.json' if original else basePathName + '.xls'
    return filePathName


# 获取当前分析文件目录完整文件名, 该文件用于记录文件分析结果
def getAnalysisFilePath(export, type, code):
    os = judgeOs()
    basePath = getBaseFileDir(os)
    symble = getSymbleByOs(os)
    basePathName = basePath + code + symble + type + symble + export + symble + export
    filePathName = basePathName + '.xls'
    return filePathName

# 获取分析文件目录
def getAnalysisPath(export, type, code):
    os = judgeOs()
    basePath = getBaseFileDir(os)
    symble = getSymbleByOs(os)
    basePathName = basePath + code + symble + type + symble + export + symble
    return basePathName

# 计算通用类指标的方法
def calCommonIndex(subject, data, indexName):
    result = 0
    index = 0
    trigger = False
    for sub in subject:
        if sub == indexName:
            trigger = True
            break
        index += 1
    if trigger:
        print('原始数据为：', data[index]),
        result = transMoney(data[index])
    else:
        result = None
    print('计算', indexName, '完成, 结果为：', result),
    return result


# 处理读出的字符中包含汉字亿和万
def transMoney(data):
    if (data == 0):
        return data
    elif (data == ''):
        return 0

    dataMoney = data.strip()
    # 包含亿万的处理方式
    if dataMoney.find(u'万亿') != -1:
        return float(dataMoney.split(u'万亿')[0]) * 1000000000000
    # 包含万的处理方式
    elif dataMoney.find(u'万') != -1:
        return float(dataMoney.split(u'万')[0]) * 10000
    # 包含亿的处理方式
    elif dataMoney.find(u'亿') != -1:
        return float(dataMoney.split(u'亿')[0]) * 100000000
    elif dataMoney.find('%') != -1:
        return float(dataMoney.split('%')[0]) / 100
    else:
        return float(data)


# 处理除数为0除法
def handleDivisionZero(data1, data2):
    if (data2 == 0):
        return 0
    else:
        return data1 / data2

# 财务信息多张图 展示图标方法和存储文件
def multiShowPlot(df, dataList, export, type, code, name):
    fig1 = plt.figure(figsize=constansEnum.Constans.FigSize.value)
    span = constansEnum.Constans.PlotXSpan.value
    x = np.array(df.columns.values.tolist()[1:span])
    print('multi x ==', x);
    cols = len(dataList)
    colCount = 1
    dfList = []
    axList = []
    for data in dataList:
        df1 = pd.DataFrame({df.values[data][0]: df.values[data][1:span]})
        dfList.append(df1)
        ax = fig1.add_subplot(cols, 1, colCount)
        axList.append(ax)
        colCount += 1

    index = 0
    for axData in axList:
        axData.set_xticks(np.arange(0, span, 1))
        axData.set_xticklabels(tuple(x))
        axData.set_title(df.values[dataList[index]][0])
        axData.plot(dfList[index], color='black', linestyle='dashed', marker='o',
                 markerfacecolor='red', markersize=5)
        index += 1
    basePath = getAnalysisPath(export, type, code)
    fileName = basePath + code + '_' + type + '_' + export + '_' + name + '.png'
    plt.savefig(fileName)

# 财务信息展示一张图，展示图标方法和存储文件
def singleShowPlot(df, dataList, export, type, code, name):
    span = constansEnum.Constans.PlotXSpan.value
    x = df.columns.values.tolist()[1:span]
    print('x ==', x)
    dataDist = {}
    count = 0
    for data in dataList:
        dataDist[df.values[data][0]] = df.values[data][1:span]
        count = len(df.values[data][1:span])
    df = pd.DataFrame(dataDist, index=x)
    # todo 实现一个x轴的时间展示数组
    df.plot(kind='bar', figsize=constansEnum.Constans.FigSize.value)
    basePath = getAnalysisPath(export, type, code)
    fileName = basePath + code + '_' + type + '_' + export + '_' + name + '.png'
    plt.savefig(fileName)

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


# 返回股票
def createStockTemp(code, industry):
    stockTemp = {'stock':code, 'industry':industry, 'createTime': datetime.datetime.now(), 'updateTime': datetime.datetime.now(),
                   'updateCount': 0, 'status': 0}
    return copy.deepcopy(stockTemp)

# 计算总股本
def getCirculateCount(gdfxInfo):
    soup = BeautifulSoup(gdfxInfo, 'lxml')
    tables = soup.findAll('table')
    special = tables[0]
    for table in soup.findAll('table'):
        for tr in table.findAll('tr'):
            for th in tr.findAll('td'):
                text = th.getText()
                if text == netEnum.Netease.circulate.value:
                    special = tr.getText()

    return int(transMoney(special.strip().split('\n')[1] + '亿'))

if __name__ == '__main__':
    # mkdir('D:\\finance\\002024\\year\\debt.xml')
    # print(getCurrentFilePath('benefit', 'report', '002024', False))
    # print(getAnalysisFilePath('analysis', 'report', '002024'))
    # print(getAnalysisPath('analysis', 'report', '002024'))
    # print(float(transMoney('1.07万亿')))
    # historicalProfitabilityEnumIndex([calcIndexEnum.CalcIndex.RetainedProfits.value, calcIndexEnum.CalcIndex.GrossProfitRate.value])
    print(np.arange(0, 10, 2))