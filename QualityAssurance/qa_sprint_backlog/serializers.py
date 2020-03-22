from rest_framework import serializers
from qa_sprint_backlog import models

class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sprint
        fields = '__all__'

class SprintRequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SprintRequirements
        fields = '__all__'