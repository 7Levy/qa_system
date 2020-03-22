from rest_framework import serializers
from qa_meeting_log import models

class MeetingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MeetingRecord
        fields = '__all__'

