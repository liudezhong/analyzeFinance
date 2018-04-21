# -*- coding: UTF-8 -*-
import requests
import json
from urllib import request
import src.base.constans.Url as UrlEnum
import src.base.constans.File as FileEnum
import src.base.commons.commonUtils as commonUtils
import src.base.file_utils.fileUtils as fileUtils

# 从互联网获取获取文件
def obtainDataFromUrl(export, type, code):
    # 转换下载地址
    downFileUrl = UrlEnum.Url.down_ths.value + code + '_' + export + '.json'
    print('抓取信息url：' + downFileUrl)
    # 定义文件名
    filePathName = commonUtils.getCurrentFilePath(export, type, code, True)
    print('总体文件名：' + filePathName)
    response = requests.get(downFileUrl, headers=UrlEnum.Url.send_headers.value)

    with open(filePathName, 'w', encoding='utf-8') as f1:
        y = response.content.decode()
        z = y.replace('{\\', '{').replace('\\"', '"').replace('\\\\', '\\').replace('\"{', '{').replace('}\"', '}')
        f1.write(z)
    print('原始抓取文件写入original文件夹成功！')

# 从同花顺获取信息并存入json文件中等待处理
def generatorOriginalFiles(code):
    fileUtils.createFileDir(code)
    # 利润表
    obtainDataFromUrl('benefit', 'year', code)
    # 现金流量表
    obtainDataFromUrl('cash', 'year', code)
    # 资产负债表
    obtainDataFromUrl('debt', 'year', code)

if __name__ =='__main__':
    generatorOriginalFiles('002024')