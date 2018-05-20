# -*- coding: UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup  # Beautiful Soup是一个可以从HTML或XML文件中提取结构化数据的Python库

# 构造头文件，模拟浏览器访问
url = "http://www.iwencai.com/stockpick/search?ts=1&f=1&qs=stockhome_topbar_click&w=600600"
url1 = "http://www.iwencai.com/stockpick/search?tid=stockpick&qs=stockpick_diag&ts=1&w=600600"
url2 = 'http://quotes.money.163.com/f10/gdfx_603589.html#01d01'
url3 = 'http://www.iwencai.com/data-robot/extract-new?query=603589&querytype=stock'
url4 = 'http://www.iwencai.com/yike/search?typed=1&preParams=&ts=1&f=1&querytype=yike&tid=info&w='+ '600600' +'&isdetail=1'
url5 = 'http://www.iwencai.com/search?typed=1&preParams=&ts=1&f=1&querytype=info&tid=info&w='+ '600600'
#<a target="_blank" href="/stockpick/search?tid=stockpick&amp;qs=stockpick_diag&amp;ts=1&amp;w=600600">青岛啤酒</a>
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
page = request.Request(url2, headers=headers)
page_info = request.urlopen(page).read().decode('utf-8')  # 打开Url,获取HttpResponse返回对象并读取其ResposneBody
print(page_info)
soup = BeautifulSoup(page_info, 'lxml')
tables = soup.findAll('table')

special = tables[0]
for table in soup.findAll('table'):
    # print(111, table)
    for tr in table.findAll('tr'):
        # print(111, tr)
        for th in tr.findAll('td'):
            # print(111, th)
            text = th.getText()
            # print(1111, text)
            if text == '流通A股(亿股)':
                special = tr.getText()
            # print(text)

print(special.strip().split('\n'))