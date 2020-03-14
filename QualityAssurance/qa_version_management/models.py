from django.db import models


class BugDetail(models.Model):
    bug_id = models.AutoField(primary_key=True)
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
    version_id = models.AutoField(primary_key=True)
    version_name = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    version_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'version_detail'
