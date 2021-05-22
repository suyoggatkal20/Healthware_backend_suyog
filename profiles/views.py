from django.shortcuts import render

from django.http import HttpResponse
# from rest_framework.views import *
from rest_framework.generics import *
from rest_framework.mixins import *
from rest_framework.response import Response
from django.db.models import *
from profiles.models import *
from profiles.Serializers import *
from rest_framework.viewsets import *
import firebase_admin
from firebase_admin import messaging


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

class DoctorCreateView(CreateAPIView):
    model = Doctor
    paginate_by = 100

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        return DoctorCreateSerializer





class RateViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingListSerializer

    def create(self, request, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class BusyViewSet(ModelViewSet):
    queryset = Busy.objects.all()
    serializer_class = BusySerializer
# env:GOOGLE_APPLICATION_CREDENTIALS="D:\Projects\DjangoTry\profile\src\google-services.json"


def call(request):
    if not firebase_admin._apps:
        firebase_admin.initialize_app()
    registration_token = 'fnibTTQdTy6h6jH3_fbb5U:APA91bEbFYtOq3F9NDoeHPqBmyHmIrF1o1Z8zFdpHKau16aZ1Iq173rLYgFDTtZdj3BeuYaH_-ZoS7joL4nLoGfQigOuuoeP428CfzsMFabwyyLtK0N4MbNdrYnss72oFIMz22StPTk0'

    # See documentation on defining a mestart.batssage payload.

    message = messaging.Message(
        data={
            'score': '850',
            'time': '2:45',
        },
        notification=messaging.Notification(
        title='Suyog',
        body='calling dhage',
    ),
        token=registration_token,
    )
    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)
    return HttpResponse('Successfully sent message:' + response)

def callend(request):
    if not firebase_admin._apps:
        firebase_admin.initialize_app()
    registration_token = 'fnibTTQdTy6h6jH3_fbb5U:APA91bEbFYtOq3F9NDoeHPqBmyHmIrF1o1Z8zFdpHKau16aZ1Iq173rLYgFDTtZdj3BeuYaH_-ZoS7joL4nLoGfQigOuuoeP428CfzsMFabwyyLtK0N4MbNdrYnss72oFIMz22StPTk0'

    # See documentation on defining a mestart.batssage payload.

    message = messaging.Message(
        data={
            'title': 'cut call',
            'when': 'now',
        },
        token=registration_token,
    )
    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)
    return HttpResponse('Successfully sent message:' + response)