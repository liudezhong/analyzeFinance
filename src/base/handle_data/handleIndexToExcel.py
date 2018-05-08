# -*- coding: UTF-8 -*-
import src.base.commons.commonUtils as commons
import src.base.constans.CalcIndex as CalcIndexEnum
import xlwings as xw
import xlwt

# 打开对应的excel，写入对应的数据
def handleIndexTemplateToExcel(datetime, export, type, code):
    #获取文件
    filePath = commons.getAnalysisFilePath(export, type, code)
    title = xlwt.Workbook()  # 创建excel对象
    sheet = title.add_sheet(export, cell_overwrite_ok=True)  # 添加一个表
    sheet.write(0, 0, '科目/日期')
    # 标题写入文件
    c = 1
    for date in datetime:
        sheet.write(0, c, date)
        c += 1
    # 时间写入文件
    c = 1
    for name, member in CalcIndexEnum.CalcIndex.__members__.items():
        print('member.value', member.value),
        sheet.write(c, 0, member.value)
        c += 1
    print('filePath = ', filePath),
    title.save(filePath)  # 保存excel

# 存入数据
def handleDataToExcel(data, col, export, type, code):
    # 获取文件
    filePath = commons.getAnalysisFilePath(export, type, code)
    app = xw.App(visible=True, add_book=False)
    app.display_alerts = False
    app.screen_updating = False
    # 文件位置：filepath，打开test文档，然后保存，关闭，结束程序
    wb = app.books.open(filePath)
    c = 1
    for index in data:
        print('index', index),
        wb.sheets[export].range('B2').value = '苦短'
        c += 1
    wb.save()
    wb.close()
    app.quit()
    print('filePath = ', filePath),

