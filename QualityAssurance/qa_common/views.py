#from django.shortcuts import render
from qa_common.models import UserLogin
from qa_common import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
from QualityAssurance import settings
import jwt
import datetime
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# Create your views here.
from qa_common.extensions.jwt_auth import JwtAuthentication,create_token
class Login(APIView):
    authentication_classes = []
    def post(self,request,format=None):
        user = request.data['account']
        pwd = request.data['password']
        queryset = UserLogin.objects.get(account=user)
        user_object = UserLogin.objects.filter(account=user, password=pwd).first()
        s = serializers.UserLoginSerializer(queryset)
        login_time = datetime.datetime.now()
        if not user_object:
            return Response({"status": "fail", "message": "账号或密码错误，请检查后重试！"})
        token = create_token({'id': user_object.id, 'user': user_object.account})
        queryset.last_login = login_time
        queryset.save()
        # s.save()
        return Response({"current_user":{"user":user,"user_id":s.data['id'],"login_time":login_time},"status": "success", "message": "登录成功","token":token,"token_prefix":""})
