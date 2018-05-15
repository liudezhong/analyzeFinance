# -*- coding: UTF-8 -*-

import src.base.obtain_data.obtainData as obtainFuc
import src.base.handle_data.handleJsonToExcel as handleFuc
import src.base.calc_index.calcIndex as calcIndexFuc
import src.base.analysis.competitiveAdvantage as comptAdvFun

def execute(code):
    obtainFuc.generatorOriginalFiles(code)
    handleFuc.allHandleDataToExcel(code)
    calcIndexFuc.calAllIndex(code)
    comptAdvFun.competitiveAdvantage(code)


if __name__ =='__main__':
    # execute('002024')
    # execute('600118')
    # execute('000002')
    # execute('002078')
    execute('600600')