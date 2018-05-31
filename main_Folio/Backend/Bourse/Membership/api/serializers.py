from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from Membership.models import MemberShip
from Bourseapp.models import Bourse
from Personapp.models import Person




class UpdateMembership(ModelSerializer):
    class Meta:
        model = MemberShip
        # fields = ('bourse','number_of_stocks_person_has')
        fields = '__all__'


class WhatPersonHave(ModelSerializer):
    class Meta:
        model = MemberShip
        # fields=('bourse','number_of_stocks_person_has')
        fields = '__all__'


class CreateMembership(ModelSerializer):
    class Meta:
        model = MemberShip
        fields = '__all__'

################### log has fk
class helpJoinBourseTable(serializers.ModelSerializer):

    class Meta:
        model = Bourse
        #fields = ('namad','lastest_Amount','lastest_Change','lastest_Percentage' )
        fields='__all__'

class What_Person_has(ModelSerializer):
    bourse=helpJoinBourseTable()
    class Meta:
        model = MemberShip
        fields=('bourse','number_of_stocks_person_has')