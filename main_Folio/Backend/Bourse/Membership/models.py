from Bourseapp.models import Bourse
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from Personapp.models import Person


class MemberShip(models.Model):
    bourse=models.ForeignKey(Bourse,on_delete=True,related_name='fk_bourse')
    person=models.ForeignKey(Person,on_delete=True,related_name='fk_person')
    number_of_stocks_person_has = models.IntegerField(default=0)