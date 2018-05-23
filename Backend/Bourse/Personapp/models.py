from django.db import models
from Bourseapp.models import Bourse


class Person(models.Model):
    username=models.TextField(primary_key=True)
    name=models.TextField(null=True,blank=True)
    #person_image=models.ImageField(null=True,blank=True)
    lastname = models.TextField()
    password=models.TextField(default="0000",null=False,blank=False)
    log_in=models.BooleanField(default=False)
    money=models.IntegerField(default='0',blank=True,null=True)
    #whatStocks=models.ManyToManyField(MemberShip)

    def __str__(self):
        return self.username

    def getMoney(self):
        return self.money

    def setMoney(self,money):
        self.money=money



class MemberShip(models.Model):
    bourse=models.ForeignKey(Bourse,on_delete=True)
    person=models.ForeignKey(Person,on_delete=True)
    person_name=models.TextField(null=True,blank=True,default=person)
    #pblist=models.ManyToManyField()
    number_of_stocks_person_has=models.IntegerField(default=0)