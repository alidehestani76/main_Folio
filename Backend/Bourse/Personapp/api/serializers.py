from rest_framework.serializers import ModelSerializer
from Personapp.models import Person,MemberShip


class UserListSerializer(ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'

class UserDetailsSerializer(ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ('username','password')


class WhatPersonHave(ModelSerializer):
    class Meta:
        model=MemberShip
        fields=('bourse','person','number_of_stocks_person_has')