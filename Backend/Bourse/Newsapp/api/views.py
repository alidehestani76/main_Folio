
from rest_framework import generics
from Newsapp.models import News

from Newsapp.api.serializers import NewsListSerializer


class NewsListAPIView (generics.ListAPIView) :
    queryset = News.objects.all()
    serializer_class = NewsListSerializer