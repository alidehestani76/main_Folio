from rest_framework.serializers import ModelSerializer
from Personapp.models import Person


class PostListSerializer(ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'

class PostDetailsSerializer(ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'