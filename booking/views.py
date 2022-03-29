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

'''
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
            user = UserModel.objects.get(username=username)
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
'''
'''
#https://ithelp.ithome.com.tw/articles/10262488?sc=iThelpR
from datetime import datetime
import json
import uuid
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_protect
from user.models import UserProfile
from django.contrib import auth     #新增
from django.contrib.sessions.models import Session#新增

#@csrf_protect
def login(request):             #登入
    if request.method == "POST":
        data = json.loads(bytes.decode(request.body,"utf-8"))
        try:
            account = data['account']
            password = data['password']
            auth_obj = auth.authenticate(username=account,password=password)#驗證帳號對錯
            if auth_obj is not None:    #驗證成功
                if request.user.is_authenticated == False:#驗證是否有帳號已登入/新增開始
                    auth_obj.check_password(password) #檢查輸入與驗證返回user對象密碼是否相符
                    request.session.create()
                    auth.login(request,auth_obj)
                    message = {"status": "登入成功"}
                else:
                    message = {"status":"帳號已登入"}
            else:
                message = {"status":"帳號密碼輸入錯誤"}
        except :
            message = {"status": "登入失敗"}
        return JsonResponse(message)
'''