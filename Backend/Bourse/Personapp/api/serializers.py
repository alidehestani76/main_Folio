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

class CreateMembership(ModelSerializer):
    class Meta:
        model = MemberShip
        fields = '__all__'


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ('username','password')

class UpdateMembership(ModelSerializer):
    class Meta:
        model = MemberShip
        #fields = ('bourse','number_of_stocks_person_has')
        fields='__all__'

class WhatPersonHave(ModelSerializer):
    class Meta:
        model=MemberShip
        #fields=('bourse','number_of_stocks_person_has')
        fields='__all__'