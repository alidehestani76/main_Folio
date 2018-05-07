from rest_framework import generics
from Personapp.models import Person
from.serializers import PostListSerializer , PostDetailsSerializer,PostCreateSerializer,PostUpdateSerializer


class PostListAPIview(generics.ListAPIView):
    #queryset = Bourse.objects.all()
    queryset = Person.objects.order_by('username')
    serializer_class = PostListSerializer


class PostDetailsAPIview(generics.RetrieveAPIView):
    lookup_field = 'username'
    queryset = Person.objects.all()
    serializer_class = PostDetailsSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PostCreateSerializer

class PostUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = Person.objects.all()
    serializer_class = PostUpdateSerializer
