
from rest_framework import generics
from Personapp.models import Person

from.serializers import UserListSerializer , UserDetailsSerializer,UserCreateSerializer,UserUpdateSerializer


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
