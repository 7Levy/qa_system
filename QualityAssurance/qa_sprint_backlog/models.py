
from django.db import models



class Sprint(models.Model):
    sprint_id = models.AutoField(primary_key=True)
    sprint_title = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    sprint_manager = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sprint'


class SprintRequirements(models.Model):
    sdemand_id = models.AutoField(primary_key=True)
    sprint_id = models.IntegerField(blank=True, null=True)
    sdemand_content = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    sdemand_partner = models.CharField(max_length=255, blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    sdemand_schedule = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sprint_requirements'

