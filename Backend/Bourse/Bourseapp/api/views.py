from rest_framework import generics
from Bourseapp.models import Bourse
from.serializers import PostListSerializer , PostDetailsSerializer

class PostListAPIview(generics.ListAPIView):
    queryset = Bourse.objects.all()
    serializer_class = PostListSerializer


class PostDetailsAPIview(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Bourse.objects.all()
    serializer_class = PostDetailsSerializer

