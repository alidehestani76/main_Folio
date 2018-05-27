from Membership.models import MemberShip
from rest_framework import generics
from Membership.api.serializers import UpdateMembership, CreateMembership, WhatPersonHave

from Membership.api.serializers import What_Person_has


class UpdateMembership(generics.UpdateAPIView):
    #lookup_fields = ('username', 'namad')

    serializer_class = UpdateMembership
    def get_object(self):
        username = self.kwargs['username']
        namad = self.kwargs['namad']
        return  MemberShip.objects.get(person=username, bourse=namad)

class CreateMembership(generics.CreateAPIView):
    queryset = MemberShip.objects.all()
    serializer_class = CreateMembership

# class WhatPersonHave(generics.ListAPIView):
#     serializer_class = WhatPersonHave
#
#     def get_queryset(self):
#         """
#         This view should return a list of all the purchases for
#         the user as determined by the username portion of the URL.
#         """
#         username = self.kwargs['username']
#         return MemberShip.objects.filter(person=username)

# class JoinTable(generics.ListAPIView):
#     queryset=MemberShip.objects.all()
#     serializer_class =UserSerializer

class JoinTable(generics.ListAPIView):
    serializer_class =  What_Person_has

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['username']
        return MemberShip.objects.filter(person=username)