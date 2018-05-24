from datetime import datetime
from Bourseapp.models import Bourse
from django.db import models



class Person(models.Model):
    username=models.TextField(primary_key=True,unique=True)
    name=models.TextField(null=True,blank=True)
    #person_image=models.ImageField(null=True,blank=True)
    lastname = models.TextField()
    password=models.TextField(default="0000",null=False,blank=False)
    log_in=models.BooleanField(default=False)
    money=models.IntegerField(default='1000',blank=True,null=True)
    male = 'm'
    female = 'f'
    gender_CHOICES = (
        (male, 'male'),
        (female, 'female'),
    )
    gender=models.CharField(max_length=20,null=True,blank=True,choices=gender_CHOICES)
    email=models.EmailField(null=True,blank=True)
    birthday=models.DateField(null=True,blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True,editable=False)

    #whatStocks=models.ManyToManyField(MemberShip)

    def __str__(self):
        return self.username

    def getMoney(self):
        return self.money

    def setMoney(self,money):
        self.money=money


