from rest_framework import serializers
from qa_common import models

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserInfo
        fields = '__all__'

class BehaviorRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BehaviorRecord
        fields = '__all__'