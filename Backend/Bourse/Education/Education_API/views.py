from rest_framework import generics


from Education.models import education
from Education.Education_API.serializers import  EduListSerializer


class EduListAPIView(generics.ListAPIView):
    queryset = education.objects.order_by('name')
    serializer_class = EduListSerializer

#
# class EduDetailsAPIView(generics.RetrieveAPIView):
#     lookup_field = 'name'
#     queryset = education.objects.all()
#     serializer_class = EduDetailsSerializer
