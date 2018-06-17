from rest_framework import generics
from Bourseapp.models import Bourse
from.serializers import StockListSerializer , StockDetailsSerializer

class StockListAPIview(generics.ListAPIView):
    #queryset = Bourse.objects.all()
    queryset = Bourse.objects.order_by('name')
    serializer_class = StockListSerializer


class StockDetailsAPIview(generics.RetrieveAPIView):
    lookup_field = 'namad'
    queryset = Bourse.objects.all()
    serializer_class = StockDetailsSerializer


