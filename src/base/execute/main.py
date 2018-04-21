# -*- coding: UTF-8 -*-

import src.base.obtain_data.obtainData as obtainFuc
import src.base.handle_data.handleJsonToExcel as handleFuc

def execute(code):
    obtainFuc.generatorOriginalFiles(code)
    handleFuc.allHandleDataToExcel(code)

if __name__ =='__main__':
    execute('002024')
    execute('600118')
    execute('000002')