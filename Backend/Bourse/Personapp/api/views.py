
from rest_framework import generics
from Personapp.models import Person,MemberShip
from rest_framework import mixins

from.serializers import UserListSerializer , UserDetailsSerializer,UserCreateSerializer,UserUpdateSerializer, \
    WhatPersonHave


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




# class WhatPersonHave(generics.RetrieveAPIView):
#     lookup_field = 'person_name'
#     queryset= MemberShip.objects.all()
#     serializer_class = WhatPersonHave



class WhatPersonHave(generics.ListAPIView):
    serializer_class = WhatPersonHave

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['username']
        return MemberShip.objects.filter(person_name=username)


