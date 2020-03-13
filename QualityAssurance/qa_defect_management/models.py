from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BugDetail(models.Model):
    title = models.CharField(max_length=32, blank=True, null=True)
    version_id = models.IntegerField(blank=True, null=True)
    presenter = models.CharField(max_length=32, blank=True, null=True)
    presenter_id = models.IntegerField(blank=True, null=True)
    assignee = models.CharField(max_length=32, blank=True, null=True)
    assignee_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    solution = models.CharField(max_length=16, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    extra_img = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bug_detail'



class VersionDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    version_name = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    version_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'version_detail'
