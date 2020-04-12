from rest_framework import serializers
from qa_interface_test import models

class AutoInterfaceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AutoInterfaceRecord
        fields = '__all__'

