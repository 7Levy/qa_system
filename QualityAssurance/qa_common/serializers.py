from rest_framework import serializers
from qa_common import models

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserLogin
        fields = '__all__'