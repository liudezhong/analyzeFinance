# -*- coding: UTF-8 -*-

from enum import Enum

class Url(Enum):
    down_ths = "http://basic.10jqka.com.cn/api/stock/finance/"
    send_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Content-Type":"text/html; charset=utf-8"}
    sina_url = "http://hq.sinajs.cn/list="