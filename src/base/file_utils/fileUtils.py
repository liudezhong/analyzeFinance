# -*- coding: UTF-8 -*-
import platform
import src.base.commons.commonUtils as commonUtils
import src.base.constans.Type as typeEnum
import src.base.constans.Export as exportEnum
import src.base.constans.Analysis as analysisEnum

import src.base.constans.File as fileDir
# 根据参数预先创建好文件夹
def createFileDir(code):
    # 获取操作系统
    os = commonUtils.judgeOs();
    # 获取基本路径
    baseDir = commonUtils.getBaseFileDir(os)
    # 获取连接符
    symble = commonUtils.getSymbleByOs(os);
    print('初始化文件目录开始')
    # 初始化文件存储路径
    for type, mem1 in typeEnum.Type.__members__.items():
        for export, mem2 in exportEnum.Export.__members__.items():
            filePath = baseDir + code + symble + mem1.value + symble + mem2.value + symble
            commonUtils.mkdir(filePath)
            print('创建文件夹：' + filePath)
        # 单独创建分析目录
        if mem1.value != typeEnum.Type.original.value:
            filePath = baseDir + code + symble + mem1.value + symble + analysisEnum.Analysis.analysis.value + symble
            commonUtils.mkdir(filePath)
    print('初始化文件目录完成')

if __name__ =='__main__':
    createFileDir('002078')