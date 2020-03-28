from rest_framework import serializers
from qa_test_case import models

class CaseSerializer(serializers.Serializer):
    class Meta:
        model = models.CaseDetail
        fields = '__all__'