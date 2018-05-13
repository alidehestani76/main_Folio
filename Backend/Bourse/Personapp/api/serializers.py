from rest_framework.serializers import ModelSerializer
from Personapp.models import Person


class UserListSerializer(ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'

class UserDetailsSerializer(ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ('username','password')

