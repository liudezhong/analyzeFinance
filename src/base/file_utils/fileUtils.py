# -*- coding: UTF-8 -*-
import platform
import src.base.commons.commonUtils as commonUtils
import src.base.constans.File as fileContans

import src.base.constans.File as fileDir
# 根据参数预先创建好文件夹
def createFileDir(export, type, code):
    # 获取操作系统
    os = commonUtils.judgeOs();
    # 获取基本路径
    baseDir = commonUtils.getBaseFileDir(os)
    # 获取连接符
    symble = commonUtils.getSymbleByOs(os);
    # 获取文件存储路径
    filePath = baseDir + code + symble + type + symble + export + symble
    commonUtils.mkdir(filePath)
    print('创建文件夹：' + filePath)
    return filePath

if __name__ =='__main__':
    createFileDir('debt', 'year', '002024')