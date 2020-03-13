from qa_common.models import UserInfo
from qa_common import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
import datetime
from qa_common.extensions.jwt_auth import JwtAuthentication, create_token
from qa_common.code import code

class Login(APIView):
    authentication_classes = []
    """
    用户登录校验
    """
    def post(self, request, format=None):
        user = request.data['account']
        pwd = request.data['password']
        queryset = UserInfo.objects.get(account=user)
        user_object = UserInfo.objects.filter(account=user, password=pwd).first()
        s = serializers.UserInfoSerializer(user_object)
        login_time = datetime.datetime.now()
        if not user_object:
            return Response({'status': {'code': code.error_2000[0], 'msg': code.error_2000[1]}})
        token = create_token({'id': user_object.id, 'user': user_object.account})
        queryset.last_login = login_time
        queryset.save()
        return Response({
            "current_user": {"user": user, "name": s.data['name'], "user_id": s.data['id'], "login_time": login_time,
                             "department_name": s.data['department_name'], "department_id": s.data['department_id'],
                             "type": s.data['type'], "position": s.data['position']},
            'status': {'code': code.sucess_code1001[0], 'msg': code.sucess_code1001[1]},
            "token": token, "token_prefix": ""
        })

class UserHub(APIView):
    authentication_classes = []
    """
    用户模块：用于查看个人资料和搜索用户
    """
    def get(self,request,user,format=None):
        user_obj = UserInfo.objects.get(id=user)
        return Response({
            "status":{"code":code.success_code[0],"msg":code.success_code[1]},
            "data":{"id":user_obj.id,"name":user_obj.name,"email":user_obj.account,"department":user_obj.department_name,"position":user_obj.position}
        })
class SearchUser(APIView):
    authentication_classes = []
    """
    模糊搜索用户
    """
    def post(self,request,format=None):
        user_list = UserInfo.objects.filter(name__contains=request.data['search_name'])
        s = serializers.UserInfoSerializer(user_list, many=True)
        return Response(s.data)
