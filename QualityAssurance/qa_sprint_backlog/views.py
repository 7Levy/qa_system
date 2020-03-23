from qa_sprint_backlog.models import Sprint,SprintRequirements
from qa_sprint_backlog import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
import datetime
from qa_common.extensions.jwt_auth import JwtAuthentication, create_token
from qa_common.code import code\


class SprintListView(APIView):
    authentication_classes = []
    def get(self,*args,**kwargs):
        sprint_query = Sprint.objects.all()
        sprint_query_s = serializers.SprintSerializer(sprint_query,many=True)
        return Response({
            'status':{'code':code.success_code[0],'msg':code.success_code[1]},
            'data':sprint_query_s.data
        })

class SprintDeatilView(APIView):
    authentication_classes = []
    def get(self,request,sprint_id,*args,**kwargs):
        sprint_query = SprintRequirements.objects.filter(sprint_id=sprint_id)
        sprint_query_s = serializers.SprintRequirementsSerializer(sprint_query,many=True)
        return Response({
            'status':{'code':code.success_code[0],'msg':code.success_code[1]},
            'data':sprint_query_s.data
        })

class DemandDeatilView(APIView):
    authentication_classes = []
    def get(self,request,demand_id,*args,**kwargs):
        demand_query = SprintRequirements.objects.get(sdemand_id=demand_id)
        demand_query_s = serializers.SprintRequirementsSerializer(demand_query)
        return Response({
            'status':{'code':code.success_code[0],'msg':code.success_code[1]},
            'data':demand_query_s.data
        })

class SprintManageView(APIView):
    authentication_classes = []
    """
    冲刺列表的操作
    """
    def post(self,request,*args,**kwargs):
        s = serializers.SprintSerializer(data=request.data)
        try:
            iterate = Sprint.objects.get(sprint_title=request.data['sprint_title'])
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
        s_query = Sprint.objects.get(sprint_id=request.data['sprint_id'])
        s = serializers.SprintSerializer(data=request.data,instance=s_query)
        if s.is_valid():
            s.save()
            return Response({
                "status": {'code': code.success_code[0], 'msg': code.success_code[1]}
            })
    def delete(self,request,*args,**kwargs):
        sprint_query = Sprint.objects.get(sprint_id=request.data['sprint_id'])
        sprint_query.delete()
        return Response({
            "status":{'code':code.success_code[0],'msg':code.success_code[1]}
        })

class SprintDemandView(APIView):
    authentication_classes = []
    """
    冲刺需求的操作
    """
    def post(self,request,*args,**kwargs):
        s = serializers.SprintRequirementsSerializer(data=request.data)
        try:
            iterate = SprintRequirements.objects.get(sdemand_content=request.data['sdemand_content'])
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
        s_query = SprintRequirements.objects.get(sdemand_id=request.data['sdemand_id'])
        s = serializers.SprintRequirementsSerializer(data=request.data,instance=s_query)
        if s.is_valid():
            s.save()
            return Response({
                "status": {'code': code.success_code[0], 'msg': code.success_code[1]}
            })
    def delete(self,request,*args,**kwargs):
        demand_query = SprintRequirements.objects.get(sdemand_id=request.data['sdemand_id'])
        demand_query.delete()
        return Response({
            "status":{'code':code.success_code[0],'msg':code.success_code[1]}
        })
