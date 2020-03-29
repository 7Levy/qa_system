from rest_framework import serializers
from qa_defect_management import models

class BugDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BugDetail
        fields = '__all__'
