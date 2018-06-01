# -*- coding: UTF-8 -*-
from urllib import request
import requests
from bs4 import BeautifulSoup  # Beautiful Soup是一个可以从HTML或XML文件中提取结构化数据的Python库
import re
# 构造头文件，模拟浏览器访问
url2 = 'http://quotes.money.163.com/f10/gdfx_603589.html#01d01'
url = 'http://quotes.money.163.com/trade/lsjysj_603589.html?year=2018&season=1'
download_url = "http://quotes.money.163.com/service/chddata.html?code=0"+"603589"+"&start="+"20150101"+"&end="+"20160231"+"&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
hy_url = "http://quotes.money.163.com/f10/hydb_600600.html"
url1 = 'http://210.21.214.18:8180/RecordingManagerService/recordingcache/1527673552646/C116881.wav'
r = requests.get(url=url1)
with open('/Users/fanpu/developer/demp.wav', 'wb') as f:
    print(1111)
    f.write(r.content)
# data = requests.get(download_url)
# print('data = ', data.text.split('\r\n')),

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
# page = request.Request(hy_url, headers=headers)
# page_info = request.urlopen(page).read().decode('utf-8')  # 打开Url,获取HttpResponse返回对象并读取其ResposneBody
# # print(page_info)
#
#
# soup = BeautifulSoup(page_info, 'lxml')
# divs = soup.findAll('div', class_='inner_box industry_info')
# print(divs)
# for div in divs:
#     for span in div.findAll('span'):
#         print(span.strong.getText())
#         if None != span.em and None != span.em.a and None != span.em.a.getText():
#             print('span.em.a.getText() = ', span.em.a.getText()),
#         if span.strong.getText().find('所属地域') >= 0:
#             print('aaa = ', span.em.a.getText())

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

# print(special.strip().split('\n'))


# test = '111g'
# if re.fullmatch(r'\d', test):
#     print('ok')
# else:
#     print('failed')
# print('a：'.find('：'))