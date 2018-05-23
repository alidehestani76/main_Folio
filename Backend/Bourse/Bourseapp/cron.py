# class a :
#     counter = 0
#     def my_scheduled_job(self):
#         print("hell")
#         self.counter+=1
#         file1 = open("/home/wt/Desktop/abbba.txt", "a")
#         file1.write("kir\n")
# test = a()
# test.my_scheduled_job()


import json
import urllib.request

from Bourseapp.models  import Bourse


class From_Bourse :
    namad=None
    name = None
    volume = None
    value = None
    count_Of_Transaction = None
    max_V = None
    min_V = None
    final_Amount = None
    final_Change = None
    final_Persentage = None
    lastest_Amount = None

    lastest_Change = None
    lastest_Percentage = None
    yesterday = None
    index_Percentage = None
    PE = None
    EPS = None
    stock_Market_Value = None
    best_Supply = None
    best_Demand = None

    def maping(self,stock):
        is_exist=Bourse.objects.filter(namad=stock.namad).exists()
        if(is_exist==True):
            obj = Bourse.objects.get(namad=stock.namad)
        else:
            obj=Bourse()
        obj.namad=stock.namad
        obj.name=stock.name
        obj.volume=stock.volume
        obj.value=stock.value
        obj.count_Of_Transaction=stock.count_Of_Transaction
        obj.max_V=stock.max_V
        obj.min_V=stock.min_V
        obj.final_Amount=stock.final_Amount
        obj.final_Change=stock.final_Change
        obj.final_Persentage=stock.final_Persentage
        obj.lastest_Amount=stock.lastest_Amount
        obj.lastest_Change =stock.lastest_Change
        obj.lastest_Percentage=stock.lastest_Percentage
        obj.yesterday =stock.yesterday
        obj.index_Percentage =stock.index_Percentage
        obj.PE=stock.PE
        obj.EPS=stock.EPS
        obj.stock_Market_Value =stock.stock_Market_Value
        obj.best_Supply=stock.best_Supply
        obj.best_Demand=stock.best_Demand
        obj.save()

    def make_Stock(self):
        with urllib.request.urlopen("http://tse.ir/json/MarketWatch/data_1.json") as url:
            data = json.loads(url.read().decode())

        stocks = []
        #for i in range(0, 270):
        for i in range(0,data["bData"].size()):
            stock = From_Bourse()
            stock.namad = data["bData"][i]["val"][0]["v"]
            stock.name = data["bData"][i]["val"][1]["v"]
            stock.volume = data["bData"][i]["val"][2]["v"]
            stock.value = data["bData"][i]["val"][3]["v"]
            stock.count_Of_Transaction = data["bData"][i]["val"][4]["v"]
            stock.max_V = data["bData"][i]["val"][5]["v"]
            stock.min_V = data["bData"][i]["val"][6]["v"]
            stock.final_Amount = data["bData"][i]["val"][7]["v"]
            stock.final_Change = data["bData"][i]["val"][8]["v"]
            stock.final_Persentage = data["bData"][i]["val"][9]["v"]
            stock.lastest_Amount = data["bData"][i]["val"][10]["v"]
            stock.lastest_Change = data["bData"][i]["val"][11]["v"]
            stock.lastest_Percentage = data["bData"][i]["val"][12]["v"]
            stock.yesterday = data["bData"][i]["val"][13]["v"]
            stock.index_Percentage = data["bData"][i]["val"][14]["v"]
            stock.PE = data["bData"][i]["val"][15]["v"]
            stock.EPS = data["bData"][i]["val"][16]["v"]
            stock.stock_Market_Value = data["bData"][i]["val"][17]["v"]
            stock.best_Supply = data["bData"][i]["val"][18]["v"]
            stock.best_Demand = data["bData"][i]["val"][19]["v"]
            stocks.append(stock)
        for stock in stocks:
            #file1 = open("/home/wt/Desktop/hasan.txt", "a")
            #file1.write(stock.name)
            self.maping(stock)




# test=From_Bourse()
# test.make_Stock()