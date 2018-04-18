from django.db import models


class Bourse(models.Model):
    name=models.TextField()
    volume=models.DecimalField(max_digits=10,decimal_places=8)
    value=models.DecimalField(max_digits=10,decimal_places=8)
    count_Of_Transaction=models.DecimalField(max_digits=10,decimal_places=8)
    max_V=models.DecimalField(max_digits=10,decimal_places=8)
    min_V=models.DecimalField(max_digits=10,decimal_places=8)
    final_Amount=models.DecimalField(max_digits=10,decimal_places=8)
    final_Change=models.DecimalField(max_digits=10,decimal_places=8)
    final_Persentage=models.FloatField()
    lastest_Amount=models.DecimalField(max_digits=10,decimal_places=8)
    lastest_Change=models.DecimalField(max_digits=10,decimal_places=8)
    lastest_Percentage=models.FloatField()
    yesterday=models.DecimalField(max_digits=10,decimal_places=8)
    index_Percentage=models.FloatField()
    PE=models.DecimalField(max_digits=10,decimal_places=8)
    EPS=models.DecimalField(max_digits=10,decimal_places=8)
    stock_Market_Value=models.DecimalField(max_digits=10,decimal_places=8)
    best_Supply=models.DecimalField(max_digits=10,decimal_places=8)
    best_Demand=models.DecimalField(max_digits=10,decimal_places=8)
    market=models.TextField()




