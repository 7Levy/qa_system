
from rest_framework.views import APIView
from rest_framework.response import Response
from qa_interface_test.interface_test import MethodGet,MethodPost,MethodPut,MethodDelete
from qa_interface_test.models import AutoInterfaceRecord
import json
import datetime
from qa_interface_test import serializers
class AutoInterfaceTest(APIView):
    authentication_classes = []
    def get(self,request,*args,**kwargs):
        query = AutoInterfaceRecord.objects.all()
        s = serializers.AutoInterfaceRecordSerializer(query,many=True)
        return Response({"data":s.data})
    def post(self,request,*args,**kwargs):
        if request.data['method']=='GET':
            method_get = MethodGet(request.data['url'])
            result = method_get.get_result()
            obj = AutoInterfaceRecord(
                method=request.data['method'],
                url=request.data['url'],
                response_body = result.json(),
                reason=result.reason,
                code=result.status_code,
                exec_time=datetime.datetime.now()
            )
            obj.save()
            return Response({
                "headers":result.headers,
                "body":result.json(),
                "cookies":result.cookies,
                "code":result.status_code,
                "reason":result.reason,
                "time":result.elapsed.microseconds/1000
            })
        elif request.data['method']=='POST':
            data = eval(request.data['body'])
            print(data)
            method_post = MethodPost(request.data['url'],data)
            result = method_post.post_result()
            obj = AutoInterfaceRecord(
                method=request.data['method'],
                url=request.data['url'],
                request_body=request.data['body'],
                response_body = result.json(),
                reason=result.reason,
                code=result.status_code,
                exec_time=datetime.datetime.now()
            )
            obj.save()
            return Response({
                "headers":result.headers,
                "body":result.json(),
                "cookies":result.cookies,
                "code":result.status_code,
                "reason":result.reason,
                "time":result.elapsed.microseconds/1000
            })
        elif request.data['method']=='PUT':
            data = eval(request.data['body'])
            print(data)
            method_put = MethodPut(request.data['url'],data)
            result = method_put.put_result()
            obj = AutoInterfaceRecord(
                method=request.data['method'],
                url=request.data['url'],
                request_body=request.data['body'],
                response_body = result.json(),
                reason=result.reason,
                code=result.status_code,
                exec_time=datetime.datetime.now()
            )
            obj.save()
            return Response({
                "headers":result.headers,
                "body":result.json(),
                "cookies":result.cookies,
                "code":result.status_code,
                "reason":result.reason,
                "time":result.elapsed.microseconds/1000
            })
        elif request.data['method'] == 'DELETE':
            data = eval(request.data['body'])
            print(data)
            method_delete = MethodDelete(request.data['url'], data)
            result = method_delete.put_result()
            obj = AutoInterfaceRecord(
                method=request.data['method'],
                url=request.data['url'],
                request_body=request.data['body'],
                response_body = result.json(),
                reason=result.reason,
                code=result.status_code,
                exec_time=datetime.datetime.now()
            )
            obj.save()
            return Response({
                "headers": result.headers,
                "body": result.json(),
                "cookies": result.cookies,
                "code": result.status_code,
                "reason": result.reason,
                "time": result.elapsed.microseconds / 1000
            })

