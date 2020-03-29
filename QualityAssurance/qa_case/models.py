
from django.db import models



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

