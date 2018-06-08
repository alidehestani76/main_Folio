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
from Newsapp.models import News
from bs4 import BeautifulSoup
import urllib.request
import datetime



class Bourse_data_access:
    def mapping(self, stock):
        is_exist = Bourse.objects.filter(namad=stock.namad).exists()
        if (is_exist == True):
            obj = Bourse.objects.get(namad=stock.namad)
        else:
            obj = Bourse()
        obj.namad = stock.namad
        obj.name = stock.name
        obj.volume = stock.volume
        obj.value = stock.value
        obj.count_Of_Transaction = stock.count_Of_Transaction
        obj.max_V = stock.max_V
        obj.min_V = stock.min_V
        obj.final_Amount = stock.final_Amount
        obj.final_Change = stock.final_Change
        obj.final_Persentage = stock.final_Persentage
        obj.lastest_Amount = stock.lastest_Amount
        obj.lastest_Change = stock.lastest_Change
        obj.lastest_Percentage = stock.lastest_Percentage
        obj.yesterday = stock.yesterday
        obj.index_Percentage = stock.index_Percentage
        obj.PE = stock.PE
        obj.EPS = stock.EPS
        obj.stock_Market_Value = stock.stock_Market_Value
        obj.best_Supply = stock.best_Supply
        obj.best_Demand = stock.best_Demand
        obj.save()


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

    # def mapping(self, stock):
    #     is_exist = Bourse.objects.filter(namad=stock.namad).exists()
    #     if (is_exist == True):
    #         obj = Bourse.objects.get(namad=stock.namad)
    #     else:
    #         obj = Bourse()
    #     obj.namad = stock.namad
    #     obj.name = stock.name
    #     obj.volume = stock.volume
    #     obj.value = stock.value
    #     obj.count_Of_Transaction = stock.count_Of_Transaction
    #     obj.max_V = stock.max_V
    #     obj.min_V = stock.min_V
    #     obj.final_Amount = stock.final_Amount
    #     obj.final_Change = stock.final_Change
    #     obj.final_Persentage = stock.final_Persentage
    #     obj.lastest_Amount = stock.lastest_Amount
    #     obj.lastest_Change = stock.lastest_Change
    #     obj.lastest_Percentage = stock.lastest_Percentage
    #     obj.yesterday = stock.yesterday
    #     obj.index_Percentage = stock.index_Percentage
    #     obj.PE = stock.PE
    #     obj.EPS = stock.EPS
    #     obj.stock_Market_Value = stock.stock_Market_Value
    #     obj.best_Supply = stock.best_Supply
    #     obj.best_Demand = stock.best_Demand
    #     obj.save()
    #
    def make_Stock(self):
        with urllib.request.urlopen("http://tse.ir/json/MarketWatch/data_1.json") as url:
            data = json.loads(url.read().decode())

        stocks = []
        #for i in range(0, 270):
        for i in range(0,len(data["bData"])):
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
            file1 = open("/home/wt/Desktop/hasanh.txt", "a")
            file1.write(stock.name)
            Bourse_data_access.mapping(self,stock)

class Newses :
    title = None
    date_day = None
    date_month = None
    date_year = None
    news_date = None
    news_Quote = None
    news_Body = None
    def mapping(self , news):
        is_exist = News.objects.filter(title=news.title).exists()
        if (is_exist == True):
            pass
            #obj = News.objects.get(title= news.title)
        else:
            obj = News()
            obj.title = news.title
            obj.date_day=news.date_day
            obj.date_month=news.date_month
            obj.date_year = news.date_year
            obj.news_date= news.news_date
            obj.news_Quote = news.news_Quote
            obj.news_Body = news.news_Body
            obj.save()

    def make_News(self):
        #news=[]
        for i in range(47830 , 47800 , -1):
            new=Newses
            try:
                fp = urllib.request.urlopen("http://tse.ir/news/newsPages/news_N"+str(i)+".html")
                mybytes = fp.read()
                mystr = mybytes.decode("utf8")
                fp.close()
                #print("i is :"+str(i))
                soup = BeautifulSoup(mystr, 'html.parser')
                now = datetime.datetime.now()
                #print(str(now))
                #title
                new.date_day=int(now.day)
                new.date_month = int(now.month)
                new.date_year = int(now.year)
                new.title=soup.title.string
                #print(soup.title.string)
                #date
                new.news_date=soup.p.text.strip()
                #print(soup.p.text.strip())
                #title
                #print(soup.h3.text.strip())
                #qoute and body
                for qute in soup.find_all('div') :
                    if qute.get('id')=='newsQuote' :
                        new.news_Quote= qute.text.strip()
                        #print(qute.text.strip())
                    if qute.get('id')=='newsBody' :
                        new.news_Body = qute.text.strip()
                        #print(qute.text.strip())
                #news.append(new)
                self.mapping(new)
                #file1 = open("/home/wt/Desktop/adeh.txt", "a")
                #file1.write(new.title)
            except urllib.error.HTTPError as f:
                continue
        #for new in news :
        #    self.mapping(new)


#Ali inja barat comment gozashtam inam crone khob ? bayad azash ye test besaazi bebini kar mikone ya na
test=Newses()
test.make_News()


#test=From_Bourse()
#test.make_Stock()