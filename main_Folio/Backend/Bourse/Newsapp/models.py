from django.db import models

# Create your models here.

class News (models.Model) :
    title = models.TextField(primary_key=True)
    date_day = models.IntegerField()
    date_month = models.IntegerField()
    date_year = models.IntegerField()
    news_date = models.TextField()
    news_Quote = models.TextField()
    news_Body = models.TextField()
