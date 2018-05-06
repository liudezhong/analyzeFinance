# -*- coding: UTF-8 -*-

import os
import platform
import src.base.constans.OSSystem as osEnum
import src.base.constans.File as fileEnum
import src.base.constans.Type as typeEnum
import src.base.constans.Benefit as benefitEnum

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
    if(os == osEnum.OSSystem.Windows.value):
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

# 计算通用类指标的方法
def calCommonIndex(data, indexName):
    result = 0
    index = 0
    trigger = False
    for name, member in benefitEnum.Benefit.__members__.items():
        if (name == indexName):  #benefitEnum.Benefit.FinanceExpense.name
            trigger = True
            break
        index += 1
    if trigger:
        result = data[index]
    else:
        result = None
    print('计算', indexName, '完成, 结果为：', result)
    return result;

if __name__ =='__main__':
    # mkdir('D:\\finance\\002024\\year\\debt.xml')
    print(getCurrentFilePath('benefit', 'report', '002024', False))