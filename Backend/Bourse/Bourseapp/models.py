from django.db import models


class Bourse(models.Model):
    name=models.TextField()
    volume=models.DecimalField()
    value=models.DecimalField()
    count_Of_Transaction=models.DecimalField()
    max_=models.DecimalField()
    min_=models.DecimalField()
    final_Amount=models.DecimalField()
    final_Change=models.DecimalField()
    final_Persentage=models.FloatField()
    lastest_Amount=models.DecimalField()
    lastest_Change=models.DecimalField()
    lastest_Percentage=models.FloatField()
    yesterday=models.DecimalField()
    index_Percentage=models.FloatField()
    PE=models.DecimalField()
    EPS=models.DecimalField()
    stock_Market_Value=models.DecimalField()
    best_Supply=models.DecimalField()
    best_Demand=models.DecimalField()
    market=models.TextField()


