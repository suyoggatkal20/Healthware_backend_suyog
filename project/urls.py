"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from profiles.views import *
from calling.views import *
from rest_framework.routers import DefaultRouter
from django.urls import include

rating_router = DefaultRouter()
rating_router.register(r'profile/rating', RateViewSet, basename='rating')
rating_router.register(r'profile/person', PersonViewSet, basename='person')
rating_router.register(r'profile/busy', BusyViewSet, basename='person')
# print(rating_router.urls)
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('patient/<int:pk>/', PatientView.as_view()),
    path('call/', call),
    path('callend/', callend),
    path('getCallDoctors/', DoctorCallingListView.as_view()),
    path('createDoctor/', DoctorCreateView.as_view()),
    path('', include(rating_router.urls))
    # DoctorListView
]
