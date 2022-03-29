import uuid

from django.core.cache import cache
from django.shortcuts import render

# Create your views here.

#from django.http import HttpResponse

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import VacancySerializer, BookingSerializer,UserSerializer
from .models import Vacancy, Booking,User

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


class UserAPI(APIView):

    def post(self, request):
        # query_params=GET
        action = request.query_params.get('action')
        if action == 'register':
            return self.do_register(request)

        elif action == 'login':
            return self.do_login(request)

    def do_register(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error_messages)

    def do_login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)
        except Exception as e:
            return Response({'msg': e})

        if not user.verify_password(password):
            return Response({'msg': 'password error!'})

        token = uuid.uuid4().hex
        print(token, uuid.uuid4())
        cache.set(token, user.id, timeout=60 * 60)
        data = {
            'msg': 'login success!',
            'status': status.HTTP_200_OK,
            'token': token,
        }

        return Response(data)