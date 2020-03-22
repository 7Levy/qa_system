from rest_framework import serializers
from qa_product_backlog import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'

class ProductRequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductRequirements
        fields = '__all__'