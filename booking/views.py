import uuid

from django.shortcuts import render

# Create your views here.

#from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import VacancySerializer, BookingSerializer,UserSerializer,BookingInquireSerializer
from .models import Vacancy, Booking,User
from django.forms import ModelForm

class VacandyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all().order_by('date')
    serializer_class = VacancySerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('date')
    serializer_class = BookingSerializer

class BookingInquireViewSet(viewsets.ModelViewSet):
    #id = request.GET.get('id', 0)
    
    lookup_field = "mobile"
    queryset = Booking.objects.all().order_by('date')
    #queryset = Booking.objects.filter(mobile__exact="0912345678").order_by('date')
    serializer_class = BookingInquireSerializer


