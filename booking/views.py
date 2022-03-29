import uuid

from django.shortcuts import render

# Create your views here.

#from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import VacancySerializer, BookingSerializer,UserSerializer
from .models import Vacancy, Booking,User

class VacandyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all().order_by('date')
    serializer_class = VacancySerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('date')
    serializer_class = BookingSerializer
