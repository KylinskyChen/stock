#!/usr/bin/python
# coding=utf-8

class sinaRealTimeData():
    '''
        实时数据；
    '''
    def __init__(self):
        self.name           = "name"            # 股票名称；
        self.open           = 11.86             # 开盘价；
        self.close          = 11.86             # 收盘价；
        self.now            = 12.08             # 当前价；
        self.high           = 12.2              # 最高价；
        self.low            = 11.76             # 最低价；
        self.buy            = 12.07             # 买入；
        self.sell           = 12.08             # 卖出；
        self.turnover       = 994413            # 成交量；
        self.volume         = 11952777.45       # 成交额；
        self.bid1_volume    = 27100             # 请求买入量；
        self.bid1           = 12.07             # 请求买入价格；      
        self.bid2_volume    = 3300      
        self.bid2           = 12.06
        self.bid3_volume    = 3200
        self.bid3           = 12.05
        self.bid4_volume    = 73200
        self.bid4           = 12.04
        self.bid5_volume    = 20400
        self.bid5           = 12.02
        self.ask1_volume    = 7000              # 请求卖出量；
        self.ask1           = 12.08             # 请求卖出价格；
        self.ask2_volume    = 1000
        self.ask2           = 12.09
        self.ask3_volume    = 11900
        self.ask3           = 12.11
        self.ask4_volume    = 8000
        self.ask4           = 12.12
        self.ask5_volume    = 2300
        self.ask5           = 12.13
        self.date           = "2021-03-01"      # 日期；
        self.time           = "15:00:03"        # 时间；

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def updateData(self, data):
        if data:
            self.srcData = data
            for item in data:
                self[item] = data[item]

    def getNow(self):
        return self.now
    def getHigh(self):
        return self.high
    def getLow(self):
        return self.low
    def getDate(self):
        return self.date
    def getTime(self):
        return self.time
    def getName(self):
        return self.name

class stock():
    def __init__(self, server = "sina"):
        # 股票代码；
        import easyquotation
        self.code = []
        self.codeNum = 0
        self.quotation = easyquotation.use(server)
        self.buyingPrice = None  # 买入价格；
        self.buyingVolume = None # 买入量；

    def setStockCode(self, code = []):
        self.code = code
        self.codeNum = len(code)
    def setBuyingPrice(self, buyingPrice):
        self.buyingPrice = buyingPrice
    def setBuyingVolume(self, buyingVolume):
        self.buyingVolume = buyingVolume
    def getBuyingPrice(self):
        return self.buyingPrice
    def getBuyingVolume(self):
        return self.buyingVolume

    def showStockName(self, name):
        print(">> name:", str(name).ljust(8))

    def showRealData(self, now, high, low, buyingPrice, buyingVolume):
        print(
            ">> high:", str(high).ljust(8), 
            str("%.2f" % (self.getYieldRate(buyingPrice, buyingVolume, high) * 100) + "%").rjust(8), 
            str("%.0f" % self.getYield(buyingPrice, buyingVolume, high)).rjust(8))
        print(
            ">> now :", 
            str(now ).ljust(8), 
            str("%.2f" % (self.getYieldRate(buyingPrice, buyingVolume, now) * 100) + "%").rjust(8), 
            str("%.0f" % self.getYield(buyingPrice, buyingVolume, now)).rjust(8))
        print(
            ">> low :", 
            str(low).ljust(8), 
            str("%.2f" % (self.getYieldRate(buyingPrice, buyingVolume, low) * 100) + "%").rjust(8),
            str("%.0f" % self.getYield(buyingPrice, buyingVolume, low)).rjust(8))

    def getYield(self, buyingPrice, buyingVolume, price):
        res = ""
        if      buyingPrice != None    \
            and buyingVolume != None   \
            and price:
            cost = buyingPrice * (0.001 + 0.003 + 0.003)
            realCapital = buyingPrice + cost
            res = (price - realCapital) * buyingVolume
        return res

    def getYieldRate(self, buyingPrice, buyingVolume, price):
        res = ""
        if      buyingPrice != None    \
            and buyingVolume != None   \
            and price:
            cost = buyingPrice * (0.001 + 0.003 + 0.003)
            realCapital = buyingPrice + cost
            Yield = price - realCapital
            res = Yield / realCapital
        return res

    def showTime(self, time):
        print(">> time:", str(time).ljust(8))

    def clearScreen(self):
        import os
        os.system("clear")

    def enterSpace(self):
        print("\n")

    def updateRealTime(self, prefix = True):
        res = False
        try:
            res = self.quotation.stocks(self.code, prefix = True) 
        except Exception:
            print(">> 获取数据失败；")
        return res

    def run(self):
        import time
        self.clearScreen()
        realData = []
        for _ in range(self.codeNum):
            realData.append(sinaRealTimeData())
        while True:
            data = self.updateRealTime()
            if data:
                self.clearScreen()
                for index, item in enumerate(data):
                    realData[index].updateData(data[item])
                    self.showStockName(realData[index].getName())
                    self.showTime(realData[index].getTime())
                    self.showRealData(
                        realData[index].getNow(), 
                        realData[index].getHigh(), 
                        realData[index].getLow(),
                        self.getBuyingPrice()[index],
                        self.getBuyingVolume()[index])
                    self.enterSpace()
            time.sleep(60)

if __name__ == "__main__":
    xcStrock = stock()
    xcStrock.setStockCode(["002159", "600250"])
    xcStrock.setBuyingPrice([12.08, 4.7])
    xcStrock.setBuyingVolume([4000 + 2100, 200])
    xcStrock.run()
