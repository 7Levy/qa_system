from qa_product_backlog.models import Product,ProductRequirements
from qa_product_backlog import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection
import datetime
from qa_common.extensions.jwt_auth import JwtAuthentication, create_token
from qa_common.code import code

class ProductListView(APIView):
    authentication_classes = []
    """
    列出产品订单的列表
    """
    def get(self,request,*args,**kwargs):
        product_query = Product.objects.all()
        product_query_s = serializers.ProductSerializer(product_query,many=True)
        return Response({
            'status':{'code':code.success_code[0],'msg':code.success_code[1]},
            'data':product_query_s.data
        })

class ProductDeatilView(APIView):
    authentication_classes = []
    """
    列出当前订单下的需求
    """
    def get(self,request,product_id,*args,**kwargs):
        product_query = ProductRequirements.objects.filter(product_id=product_id)
        product_query_s = serializers.ProductRequirementsSerializer(product_query,many=True)
        return Response({
            'status':{'code':code.success_code[0],'msg':code.success_code[1]},
            'data':product_query_s.data
        })

class DemandDeatilView(APIView):
    authentication_classes = []
    """
    展示当前需求的详情
    """
    def get(self,request,demand_id,*args,**kwargs):
        demand_query = ProductRequirements.objects.get(demand_id=demand_id)
        demand_query_s = serializers.ProductRequirementsSerializer(demand_query)
        return Response({
            'status':{'code':code.success_code[0],'msg':code.success_code[1]},
            'data':demand_query_s.data
        })

class ProductManageView(APIView):
    authentication_classes = []
    """
    产品列表的操作
    """
    def post(self,request,*args,**kwargs):
        s = serializers.ProductSerializer(data=request.data)
        try:
            iterate = Product.objects.get(product_title=request.data['product_title'])
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
        s_query = Product.objects.get(product_id=request.data['product_id'])
        s = serializers.ProductSerializer(data=request.data,instance=s_query)
        if s.is_valid():
            s.save()
            return Response({
                "status": {'code': code.success_code[0], 'msg': code.success_code[1]}
            })
    def delete(self,request,*args,**kwargs):
        bug_query = Product.objects.get(product_id=request.data['product_id'])
        bug_query.delete()
        return Response({
            "status":{'code':code.success_code[0],'msg':code.success_code[1]}
        })

class ProductDemandView(APIView):
    authentication_classes = []
    """
    产品需要的操作
    """
    def post(self,request,*args,**kwargs):
        s = serializers.ProductRequirementsSerializer(data=request.data)
        try:
            iterate = ProductRequirements.objects.get(demanid_content=request.data['demand_content'])
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
        s_query = ProductRequirements.objects.get(demand_id=request.data['demand_id'])
        s = serializers.ProductRequirementsSerializer(data=request.data,instance=s_query)
        if s.is_valid():
            s.save()
            return Response({
                "status": {'code': code.success_code[0], 'msg': code.success_code[1]}
            })
    def delete(self,request,*args,**kwargs):
        product_query = ProductRequirements.objects.get(demand_id=request.data['demand_id'])
        product_query.delete()
        return Response({
            "status":{'code':code.success_code[0],'msg':code.success_code[1]}
        })