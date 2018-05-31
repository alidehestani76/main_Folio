from serializers import NewsListSerializer
from rest_framework import generics
from Newsapp.models import News

class NewsListAPIView (generics.ListAPIView) :
    queryset = News.objects.all()
    serializer_class = NewsListSerializer