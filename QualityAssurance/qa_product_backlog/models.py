

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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

