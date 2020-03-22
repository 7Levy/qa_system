from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
class GetCurrentTime(APIView):
    authentication_classes = []
    def get(self,*args,**kwargs):
        current_time = datetime.datetime.now()
        return Response({
            "current_time":current_time
        })