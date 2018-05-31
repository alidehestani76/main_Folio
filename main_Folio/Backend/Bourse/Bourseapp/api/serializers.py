from rest_framework.serializers import ModelSerializer
from Bourseapp.models import Bourse


class PostListSerializer(ModelSerializer):
    class Meta:
        model=Bourse
        fields='__all__'

class PostDetailsSerializer(ModelSerializer):
    class Meta:
        model=Bourse
        fields='__all__'