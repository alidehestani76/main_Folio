from rest_framework.serializers import ModelSerializer
from Education.models import education


class EduListSerializer(ModelSerializer):
    class Meta:
        model = education
        fields = '__all__'
#
#
# class EduDetailsSerializer(ModelSerializer):
#     class Meta:
#         model = education
#         fields = '__all__'
#
#
