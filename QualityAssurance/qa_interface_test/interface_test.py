import requests   #导入requests模块
# params = {
# 		 'meeting_title':'立会2',
# 		 'meeting_content':'内容2',
# 		 'meeting_time':'2020-03-22 16:02:00'
# 		}
# response=requests.post("http://175.24.45.188:8080/api/meeting/record/management",json=params)
# print(response.cookies)
# print(response.elapsed.microseconds)

class MethodGet:
    def __init__(self,url):
        self.url = url
    def get_json_text(self):
        response = requests.get(self.url)
        return response.json()
    def get_content(self):
        response = requests.get(self.url)
        return response.content
    def get_headers(self):
        response = requests.get(self.url)
        return response.headers
    def get_cookie(self):
        response = requests.get(self.url)
        return response.cookies
    def get_result(self):
        response = requests.get(self.url)
        return response
class MethodPost:
    def __init__(self,url,data):
        self.url = url
        self.data = data
    def post_result(self):
        response = requests.post(self.url,json=self.data)
        return response
class MethodPut:
    def __init__(self,url,data):
        self.url = url
        self.data = data
    def put_result(self):
        response = requests.put(self.url,json=self.data)
        return response

class MethodDelete:
    def __init__(self,url,data):
        self.url = url
        self.data = data
    def put_result(self):
        response = requests.delete(self.url,json=self.data)
        return response
