from rest_framework import serializers

from booking.models import Vacancy, Booking,User

class VacancySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'

class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'