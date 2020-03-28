from qa_meeting_log.models import MeetingRecord
from qa_meeting_log import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
import datetime
from qa_common.extensions.jwt_auth import JwtAuthentication, create_token
from qa_common.code import code

class MeetingListView(APIView):
    authentication_classes = []
    """
    获取立会列表
    """
    def get(self,*args,**kwargs):
        record_query = MeetingRecord.objects.all()
        record_query_s = serializers.MeetingRecordSerializer(record_query,many=True)
        return Response({
            'status':{'code':code.success_code[0],'msg':code.success_code[1]},
            'data':record_query_s.data
        })

class MeetingDetailView(APIView):
    authentication_classes = []
    """
    获取某个立会的详情
    """
    def get(self,request,meeting_id,*args,**kwargs):
        meeting_query = MeetingRecord.objects.get(meeting_id=meeting_id)
        meeting_query_s = serializers.MeetingRecordSerializer(meeting_query)
        return Response({
            'status':{'code':code.success_code[0],'msg':code.success_code[1]},
            'data':meeting_query_s.data
        })

class MeetingManageView(APIView):
    authentication_classes = []
    """
    会议记录的操作
    """
    def post(self,request,*args,**kwargs):
        s = serializers.MeetingRecordSerializer(data=request.data)
        try:
            iterate = MeetingRecord.objects.get(meeting_title=request.data['meeting_title'])
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
        s_query = MeetingRecord.objects.get(meeting_id=request.data['meeting_id'])
        s = serializers.MeetingRecordSerializer(data=request.data,instance=s_query)
        if s.is_valid():
            s.save()
            return Response({
                "status": {'code': code.success_code[0], 'msg': code.success_code[1]}
            })
    def delete(self,request,*args,**kwargs):
        bug_query = MeetingRecord.objects.get(meeting_id=request.data['meeting_id'])
        bug_query.delete()
        return Response({
            "status":{'code':code.success_code[0],'msg':code.success_code[1]}
        })