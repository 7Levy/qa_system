from qa_defect_management.models import BugDetail,VersionDetail
from qa_defect_management import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
import datetime
from qa_common.extensions.jwt_auth import JwtAuthentication, create_token
from qa_common.code import code
from qa_common.extensions.pagination import LimitOffset

class BugListView(APIView):
    authentication_classes = []
    """
    BUG列表
    """
    def get(self,request,version_id,*args,**kwargs):
        bug_query = BugDetail.objects.filter(version_id=version_id)
        bug_count = bug_query.count()
        page_obj = LimitOffset()
        bug_page = page_obj.paginate_queryset(queryset=bug_query,request=request,view=self)
        bug_list = serializers.BugDetailSerializer(bug_page,many=True)
        return Response({
            'total':bug_count,
            'status':{'code':code.success_code[0],'msg':code.success_code[1]},
            'data':bug_list.data
        })

class BugDetailView(APIView):
    authentication_classes = []
    """
    BUG详细信息
    """
    def get(self,request,bug_id,*args,**kwargs):
        bug_detail_query = BugDetail.objects.get(bug_id=bug_id)
        bug_detail = serializers.BugDetailSerializer(bug_detail_query)
        return Response({
            'status':{'code':code.success_code[0],'msg':code.success_code[1]},
            'data':bug_detail.data
        })

class BugManageView(APIView):
    authentication_classes = []
    """
    BUG管理：新建BUG、编辑BUG、删除BUG
    """
    def post(self,request,*args,**kwargs):
        s = serializers.BugDetailSerializer(data=request.data)
        try:
            duplicate_title = BugDetail.objects.get(title=request.data['title'])
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
        s_query = BugDetail.objects.get(bug_id=request.data['bug_id'])
        s = serializers.BugDetailSerializer(data=request.data,instance=s_query)
        if s.is_valid():
            s.save()
            return Response({
                "status": {'code': code.success_code[0], 'msg': code.success_code[1]}
            })
    def delete(self,request,*args,**kwargs):
        bug_query = BugDetail.objects.get(bug_id=request.data['bug_id'])
        bug_query.delete()
        return Response({
            "status":{'code':code.success_code[0],'msg':code.success_code[1]}
        })
