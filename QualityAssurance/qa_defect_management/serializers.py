from rest_framework import serializers
from qa_defect_management import models

class BugDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BugDetail
        fields = '__all__'

class VersionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VersionDetail
        fields = '__all__'