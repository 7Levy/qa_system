from qa_version_management import models
from rest_framework import serializers

class VersionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VersionDetail
        fields = '__all__'