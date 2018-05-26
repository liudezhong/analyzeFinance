# -*- coding: UTF-8 -*-
from urllib import request
import requests
from bs4 import BeautifulSoup  # Beautiful Soup是一个可以从HTML或XML文件中提取结构化数据的Python库
import re
# 构造头文件，模拟浏览器访问
url2 = 'http://quotes.money.163.com/f10/gdfx_603589.html#01d01'
url = 'http://quotes.money.163.com/trade/lsjysj_603589.html?year=2018&season=1'
download_url = "http://quotes.money.163.com/service/chddata.html?code=1"+"603589"+"&start="+"20150101"+"&end="+"20160101"+"&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"

data = requests.get(download_url)
print('data = ', data.text.split('\r\n')),

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
# page = request.Request(download_url, headers=headers)
# page_info = request.urlopen(page).read().decode('utf-8')  # 打开Url,获取HttpResponse返回对象并读取其ResposneBody
# print(page_info)


# soup = BeautifulSoup(page_info, 'lxml')
# tables = soup.findAll('table')
#
# special = tables[0]
# for table in soup.findAll('table'):
#     # print(111, table)
#     for tr in table.findAll('tr'):
#         # print(111, tr)
#         for th in tr.findAll('td'):
#             # print(111, th)
#             text = th.getText()
#             # print(1111, text)
#             if text == '流通A股(亿股)':
#                 special = tr.getText()
#             # print(text)
#
# print(special.strip().split('\n'))


# test = '111g'
# if re.fullmatch(r'\d', test):
#     print('ok')
# else:
#     print('failed')