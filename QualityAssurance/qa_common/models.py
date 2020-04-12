# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AutoInterfaceRecord(models.Model):
    test_id = models.AutoField(primary_key=True)
    method = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    request_body = models.CharField(max_length=255, blank=True, null=True)
    response_body = models.CharField(max_length=255, blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    exec_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auto_interface_record'


class BehaviorRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    ip_addr = models.CharField(max_length=255, blank=True, null=True)
    behavior = models.CharField(max_length=255, blank=True, null=True)
    behavior_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'behavior_record'


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


class CaseDetail(models.Model):
    case_id = models.AutoField(primary_key=True)
    version_id = models.IntegerField(blank=True, null=True)
    case_name = models.CharField(max_length=255, blank=True, null=True)
    module = models.CharField(max_length=32, blank=True, null=True)
    function = models.CharField(max_length=32, blank=True, null=True)
    case_content = models.CharField(max_length=255, blank=True, null=True)
    precondition = models.CharField(max_length=255, blank=True, null=True)
    steps = models.CharField(max_length=255, blank=True, null=True)
    expected_result = models.CharField(max_length=255, blank=True, null=True)
    self_test_result = models.IntegerField(db_column='self_test result', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    actual_result = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case_detail'


class MeetingRecord(models.Model):
    meeting_id = models.AutoField(primary_key=True)
    meeting_title = models.CharField(max_length=32, blank=True, null=True)
    meeting_content = models.CharField(max_length=255, blank=True, null=True)
    meeting_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meeting_record'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_title = models.CharField(max_length=64, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    product_manager = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class ProductRequirements(models.Model):
    demand_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField(blank=True, null=True)
    demand_content = models.CharField(max_length=32, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    demand_status = models.IntegerField(blank=True, null=True)
    demand_type = models.CharField(max_length=32, blank=True, null=True)
    demand_priority = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_requirements'


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


class UserInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16, blank=True, null=True)
    account = models.CharField(max_length=64, blank=True, null=True)
    password = models.CharField(max_length=16, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    department_name = models.CharField(max_length=16, blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_info'


class VersionDetail(models.Model):
    version_id = models.AutoField(primary_key=True)
    version_name = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    version_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'version_detail'
