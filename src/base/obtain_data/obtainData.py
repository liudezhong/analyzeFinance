# -*- coding: UTF-8 -*-
import requests

import src.base.commons.commonUtils as commonUtils
import src.base.constans.Url as UrlEnum
import src.base.file_utils.fileUtils as fileUtils


# 从互联网获取获取文件
def obtainDataFromUrl(export, code):
    # 转换下载地址
    downFileUrl = UrlEnum.Url.down_ths.value + code + '_' + export + '.json'
    print('抓取信息url：' + downFileUrl)
    # 定义文件名
    filePathName = commonUtils.getCurrentFilePath(export, None, code, True)
    print('总体文件名：' + filePathName)
    response = requests.get(downFileUrl, headers=UrlEnum.Url.send_headers.value)

    with open(filePathName, 'w', encoding='utf-8') as f1:
        y = response.content.decode()
        z = y.replace('{\\', '{').replace('\\"', '"').replace('\\\\', '\\').replace('\"{', '{').replace('}\"', '}')
        f1.write(z)
    print('原始抓取文件写入original文件夹成功！')

# 从同花顺获取信息并存入json文件中等待处理
def generatorOriginalFiles(code):
    # 初始化文件目录
    fileUtils.createFileDir(code)
    # 利润表
    obtainDataFromUrl('benefit', code)
    # 现金流量表
    obtainDataFromUrl('cash', code)
    # 资产负债表
    obtainDataFromUrl('debt', code)
    # 主要指标
    obtainDataFromUrl('main', code)
    # 每股能力
    obtainDataFromUrl('each', code)
    # 成长能力
    obtainDataFromUrl('grow', code)
    # 偿债能力
    obtainDataFromUrl('pay', code)
    # 运营能力
    obtainDataFromUrl('operate', code)




if __name__ =='__main__':
    generatorOriginalFiles('002024')