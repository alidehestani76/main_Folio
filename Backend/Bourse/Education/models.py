from django.db import models

# Create your models here.

class education (models.Model) :
    name = models.TextField(primary_key=True,null=False)
    length=models.TextField(null=True)
    date=models.DateField(null=True)
    size=models.TextField(null=True)
    link=models.TextField(null=False)
    detail=models.TextField(null=True)