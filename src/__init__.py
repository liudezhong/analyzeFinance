# -*- coding: UTF-8 -*-
import platform
def processStr(s):
    x = str(s).replace(' ','');
    return x

if __name__ =='__main__':
    print (processStr("在 盘整 行情 中， 应以 观望 为主， 宁可 错过， 不可 做错。 "))
    print (platform.system())