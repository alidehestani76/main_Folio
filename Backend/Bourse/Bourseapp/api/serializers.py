from rest_framework.serializers import ModelSerializer
from Bourseapp.models import Bourse


class StockListSerializer(ModelSerializer):
    class Meta:
        model=Bourse
        fields='__all__'

class StockDetailsSerializer(ModelSerializer):
    class Meta:
        model=Bourse
        fields='__all__'