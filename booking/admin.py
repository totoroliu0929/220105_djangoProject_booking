from django.contrib import admin

# Register your models here.

from .models import Vacancy, User, Booking
admin.site.register(Vacancy)
admin.site.register(User)
admin.site.register(Booking)
