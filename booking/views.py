from django.shortcuts import render

# Create your views here.

#from django.http import HttpResponse

from rest_framework import viewsets
from .serializers import VacancySerializer, BookingSerializer
from .models import Vacancy, Booking

class VacandyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all().order_by('date')
    serializer_class = VacancySerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('date')
    serializer_class = BookingSerializer



"""
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("pwd")
    user_obj = models.UserInfo.objects.filter(username=username, password=password).first()
    print(user_obj.username)

    if not user_obj:
        return redirect("/session_login/")
    else:
        request.session['is_login'] = True
        request.session['user1'] = username
        return redirect("/s_index/")

def s_index(request):
    status = request.session.get('is_login')
    if not status:
        return redirect('/session_login/')
    return render(request, "s_index.html")

def s_logout(request):
    # del request.session["is_login"] # 删除session_data里的一组键值对
    request.session.flush() # 删除一条记录包括(session_key session_data expire_date)三个字段
    return redirect('/session_login/')
"""