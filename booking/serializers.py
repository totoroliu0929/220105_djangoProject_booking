from rest_framework import serializers

from booking.models import Vacancy, Booking

class VacancySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vacancy
        filds = '__all__'

class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        filds = '__all__'