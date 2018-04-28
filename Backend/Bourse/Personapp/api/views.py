from rest_framework import generics
from Personapp.models import Person
from.serializers import PostListSerializer , PostDetailsSerializer

class PostListAPIview(generics.ListAPIView):
    #queryset = Bourse.objects.all()
    queryset = Person.objects.order_by('username')
    serializer_class = PostListSerializer


class PostDetailsAPIview(generics.RetrieveAPIView):
    lookup_field = 'username'
    queryset = Person.objects.all()
    serializer_class = PostDetailsSerializer


