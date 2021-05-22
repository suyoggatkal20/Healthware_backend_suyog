# django
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from django.db.models import *
# from rest_framework
from rest_framework.generics import *
from rest_framework.mixins import *
from rest_framework.response import Response
from rest_framework.viewsets import *
#firebase
import firebase_admin
from firebase_admin import messaging
# my
from profiles.models import *
from calling.Serializers import *


from datetime import datetime  
from datetime import timedelta  


class DoctorCallingListView(ListAPIView):
    model = Doctor
    paginate_by = 100
    serializer_class = DoctorListSerializer;
    def get_queryset(self):
        max_price = self.request.GET.get('max_price')
        min_price = self.request.GET.get('min_price')
        min_rating = self.request.GET.get('min_rating')
        max_rating = self.request.GET.get('max_rating')
        min_exp = self.request.GET.get('min_exp')
        max_exp = self.request.GET.get('max_exp')
        name_search = self.request.GET.get('name_search')
        print(Doctor)
        queryset = Doctor.objects.all()
        queryset = queryset.annotate(avg_rating=Avg('rating__rating'))
        #queryset = queryset.prefetch_related('email')
        queryset = queryset.prefetch_related('phone')
        #queryset = queryset.prefetch_related('address')
        queryset = queryset.prefetch_related('emergency_contact')
        #queryset = queryset.prefetch_related('other')
        #queryset = queryset.prefetch_related('busy')
        #queryset = queryset.prefetch_related('slot')
        if min_price:
            queryset=queryset.filter(charge_per_app__gte=min_price)
        if max_price:
            queryset=queryset.filter(charge_per_app__lte=max_price)
        if min_rating:
            queryset=queryset.filter(avg_rating__gte=min_rating)
        if max_rating:
            queryset=queryset.filter(avg_rating__lte=max_rating)
        if min_exp:
            queryset=queryset.filter(practice_started__lte=(datetime.now()-timedelta(seconds=31556952*int(min_exp))))
        if max_exp:
            exp=(datetime.now()-timedelta(seconds=31556952*int(max_exp)))
            print('suyog : ',exp,datetime.now())
            queryset=queryset.filter(practice_started__gte=exp)
        if name_search:
            queryset=queryset.filter(Q(first_name__icontains=name_search)| Q(last_name__icontains=name_search))
        return queryset



def call(request):
    if not firebase_admin._apps:
        firebase_admin.initialize_app()
    pk=request.POST.get('pk')
    registration_token = 'fnibTTQdTy6h6jH3_fbb5U:APA91bEbFYtOq3F9NDoeHPqBmyHmIrF1o1Z8zFdpHKau16aZ1Iq173rLYgFDTtZdj3BeuYaH_-ZoS7joL4nLoGfQigOuuoeP428CfzsMFabwyyLtK0N4MbNdrYnss72oFIMz22StPTk0';
    registration_token=Person.objects.filter(pk=pk)['token']
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
    return HttpResponse('Successfully sent message:'+response)

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