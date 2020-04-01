from rest_framework import serializers
from qa_case import models

class CaseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CaseDetail
        fields = '__all__'