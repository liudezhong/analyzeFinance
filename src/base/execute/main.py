# -*- coding: UTF-8 -*-

import src.base.obtain_data.obtainData as obtainFuc
import src.base.handle_data.handleJsonToExcel as handleFuc
import src.base.calc_index.calcIndex as calcIndexFuc
import src.base.analysis.competitiveAdvantage as comptAdvFuc
import src.base.analysis.analysisGrow as analyGrowFuc
import src.base.analysis.theForProfit as forProfitFuc
import src.base.analysis.financialHealth as finanHealthFuc

def execute(code):
    # TODO 后期再加上这个数据库的初始化操作，先实现报表的统计计量
    obtainFuc.generatorOriginalFiles(code)
    handleFuc.allHandleDataToExcel(code)
    calcIndexFuc.calAllIndex(code)
    comptAdvFuc.competitiveAdvantage(code)
    analyGrowFuc.calGrowth(code)
    forProfitFuc.calPercentageProfitStatement(code)
    finanHealthFuc.calfinancialHealth(code)



if __name__ =='__main__':
    execute('002024')
    execute('600118')
    execute('000002')
    execute('002078')
    execute('600600')
    execute('300438')
    execute('000635')
