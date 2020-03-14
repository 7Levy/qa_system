from qa_version_management.models import BugDetail,VersionDetail
from qa_version_management import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
import datetime
from qa_common.extensions.jwt_auth import JwtAuthentication, create_token
from qa_common.code import code
from qa_common.extensions.pagination import LimitOffset

class VersionManagement(APIView):
    authentication_classes = []
    """
    版本管理
    """
    def get(self,*args,**kwargs):
        version_query = VersionDetail.objects.all()
        version_list  = serializers.VersionDetailSerializer(version_query,many=True)
        version_count = version_query.count()
        return Response({
            "total":version_count,
            "status":{'code':code.success_code[0],'msg':code.success_code[1]},
            "data":version_list.data
        })

    def post(self,request,*args,**kwargs):
        s = serializers.VersionDetailSerializer(data=request.data)
        try:
            duplicate_version = VersionDetail.objects.get(version_name=request.data['version_name'])
            return Response({
                "status":{'code':code.error_2006[0],'msg':code.error_2006[1]}
            })
        except:
            if s.is_valid():
                s.save()
                return Response({
                    "status":{'code':code.success_code[0],'msg':code.success_code[1]}
                })
    def put(self,request,*args,**kwargs):
        version_query = VersionDetail.objects.get(version_id=request.data['version_id'])
        version_s = serializers.VersionDetailSerializer(data=request.data,instance=version_query)
        if version_s.is_valid():
            version_s.save()
            return Response({
                "status": {'code': code.success_code[0], 'msg': code.success_code[1]}
            })
    def delete(self,request,*args,**kwargs):
        version_query = VersionDetail.objects.get(version_id=request.data['version_id'])
        version_query.delete()
        return Response({
            "status":{'code':code.success_code[0],'msg':code.success_code[1]}
        })