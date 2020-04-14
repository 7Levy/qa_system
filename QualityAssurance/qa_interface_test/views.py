
from rest_framework.views import APIView
from rest_framework.response import Response
from qa_interface_test.interface_test import MethodGet,MethodPost,MethodPut,MethodDelete
from qa_interface_test.models import AutoInterfaceRecord
from qa_common.models import UserInfo
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import datetime
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


class ExecRecordTest(APIView):
    authentication_classes = []
    def get(self,request,test_id,*args,**kwargs):
        test_case = AutoInterfaceRecord.objects.get(test_id=test_id)
        if test_case.method == 'GET':
            method_get = MethodGet(test_case.url)
            result = method_get.get_result()
            test_case.exec_time = datetime.datetime.now()
            test_case.save()
            return Response({
                "headers": result.headers,
                "body": result.json(),
                "cookies": result.cookies,
                "code": result.status_code,
                "reason": result.reason,
                "time": result.elapsed.microseconds / 1000
            })


class SendMail(APIView):
    authentication_classes = []
    def get(self,request,receiver_id,*args,**kwargs):
        ret = True
        security_account = '1571645388@qq.com'
        security_password = 'uyltirninhczjige'
        re_obj = UserInfo.objects.get(id=receiver_id)
        receiver = re_obj.account
        try:
            result = []
            query = AutoInterfaceRecord.objects.all()
            s = serializers.AutoInterfaceRecordSerializer(query,many=True)
            data = list(s.data)
            for i in range(len(data)):
                msg = str(i+1)+".用例编号"+"["+str(data[i]['test_id'])+"]："+str(data[i]['url'])+" 执行结果为-》"+str(data[i]['reason'])+"接口状态-》"+str(data[i]['code'])+'\r\n'
                result.append(msg)
            result = ''.join(result)
            msg = MIMEText("技术团队的成员大家好，本次汇报结果由机器人小e完成："+'\r\n'+str(result), 'plain', 'utf-8')
            msg['From'] = formataddr(["来自方圻程", security_account])
            msg['To'] = formataddr(["发送至研发团队", receiver])
            msg['Subject'] = "测试执行日期" + str(datetime.datetime.now())
            server = smtplib.SMTP_SSL("smtp.qq.com", 465)
            server.login(security_account, security_password)
            server.sendmail(security_account, [receiver, ], msg.as_string())
            server.quit()
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret = False
        if ret:
            return Response({"msg":"邮件发送成功!"})
        else:
            return Response({"msg":"邮件发送失败，请检查接收邮件账号是否开启smtp服务!"})