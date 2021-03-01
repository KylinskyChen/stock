#!/usr/bin/python
# coding=utf-8

import easyquotation
import time

class stock():
    def __init__(self, code):
        # 股票代码；
        self.code = code

    class realTimeData():
        '''
            实时数据；
        '''
        def __init__(self):
            self.name           = "name"            # 股票名称；
            self.open           = 11.86             # 开盘价格；
            self.close          = 11.86             
            self.now            = 12.08
            self.high           = 12.2
            self.low            = 11.76
            self.buy            = 12.07
            self.sell           = 12.08
            self.turnover       = 994413
            self.volume         = 11952777.45
            self.bid1_volume    = 27100
            self.bid1           = 12.07
            self.bid2_volume    = 3300
            self.bid2           = 12.06
            self.bid3_volume    = 3200
            self.bid3           = 12.05
            self.bid4_volume    = 73200
            self.bid4           = 12.04
            self.bid5_volume    = 20400
            self.bid5           = 12.02
            self.ask1_volume    = 7000
            self.ask1           = 12.08
            self.ask2_volume    = 1000
            self.ask2           = 12.09
            self.ask3_volume    = 11900
            self.ask3           = 12.11
            self.ask4_volume    = 8000
            self.ask4           = 12.12
            self.ask5_volume    = 2300
            self.ask5           = 12.13
            self.date           = "2021-03-01"
            self.time           = "15:00:03"

    def updateRealTime(self, *code, prefix = True):
        return quotation.stocks(list(code), prefix = True) 

    def run(self):
        while True:
            self.updateRealTime(self.code)
            time.sleep(60)

if __name__ == "__main__":

    quotation = easyquotation.use('sina')

    while True:
        data = quotation.stocks(['002159'], prefix = True) 
        print(data)
