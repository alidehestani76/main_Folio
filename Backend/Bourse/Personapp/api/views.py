from django_common import session
from requests import Session
from requests import request
from rest_framework import generics
from Personapp.models import Person

from .serializers import UserListSerializer, UserDetailsSerializer, UserCreateSerializer, UserUpdateSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = Person.objects.order_by('username')
    serializer_class = UserListSerializer


class UserDetailsAPIView(generics.RetrieveAPIView):
    #session = Session.objects.get(session_key=session_key)
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
