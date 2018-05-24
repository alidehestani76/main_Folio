from rest_framework.serializers import ModelSerializer

from Membership.models import MemberShip


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
