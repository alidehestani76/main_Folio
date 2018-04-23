from django.db import models


class Bourse(models.Model):
    name=models.TextField(null=True,blank=True)
    namad=models.TextField(primary_key=True,null=False,blank=False,default="none")
    volume=models.TextField(null=True,blank=True,default=0)
    value=models.TextField(null=True,blank=True)
    count_Of_Transaction=models.TextField(null=True,blank=True)
    max_V=models.TextField(null=True,blank=True)
    min_V=models.TextField(null=True,blank=True)
    final_Amount=models.TextField(null=True,blank=True)
    final_Change=models.TextField(null=True,blank=True)
    final_Persentage=models.TextField(null=True,blank=True)
    lastest_Amount=models.TextField(null=True,blank=True)
    lastest_Change=models.TextField(null=True,blank=True)
    lastest_Percentage=models.TextField(null=True,blank=True)
    yesterday=models.TextField(null=True,blank=True)
    index_Percentage=models.TextField(null=True,blank=True)
    PE=models.TextField(null=True,blank=True)
    EPS=models.TextField(null=True,blank=True)
    stock_Market_Value=models.TextField(null=True,blank=True)
    best_Supply=models.TextField(null=True,blank=True)
    best_Demand=models.TextField(null=True,blank=True)
    market=models.TextField(null=True,blank=True)




