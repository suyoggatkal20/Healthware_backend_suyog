from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import *
from rest_framework.response import Response

from profiles.models import *
from profiles.Serializers import *
from django.views.generic.list import ListView;
# Create your views here.

# path('bsjh/<int:year>/',


# class PatientView(APIView):

#     def get(self, request, pk):
#         result = model.objects.get(pk=pk)
#         serial = serializer(result)
#         print(serial.data)
#         return serial.data

#     def get(self, request):
#         result = Patient.objects.all()
#         serial = PatientSerializer(result, many=True)
#         print(serial.data)
#         return Response(serial.data)

#     def post(self, request):
#         pass



class PatientView(GenericAPIView,ListModelMixing,CreateModelMixing,RetriveModelMixing):
    model=Patient
    paginate_by = 100

