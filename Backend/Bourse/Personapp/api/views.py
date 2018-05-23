
from rest_framework import generics
from Personapp.models import Person,MemberShip
from Bourseapp.models import Bourse

from.serializers import UserListSerializer , UserDetailsSerializer,UserCreateSerializer,UserUpdateSerializer, \
    WhatPersonHave,UpdateMembership,CreateMembership


class UserListAPIview(generics.ListAPIView):
    #queryset = Bourse.objects.all()
    queryset = Person.objects.order_by('username')
    serializer_class = UserListSerializer


class UserDetailsAPIview(generics.RetrieveAPIView):
    lookup_field = 'username'
    queryset = Person.objects.all()

    serializer_class = UserDetailsSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = UserCreateSerializer

class UserUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = 'username'
    queryset = Person.objects.all()
    serializer_class = UserUpdateSerializer

# class UpdateMembership(generics.UpdateAPIView):
#     lookup_fields = ('username', 'boursename')
#     serializer_class = UpdateMembership
#     def get_queryset(self):
#         username = self.kwargs['username']
#         boursename = self.kwargs['boursename']
#         return  MemberShip.objects.filter(person=username, bourse=boursename)


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




class WhatPersonHave(generics.ListAPIView):
    serializer_class = WhatPersonHave

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['username']
        return MemberShip.objects.filter(person=username)


