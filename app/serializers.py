from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        # fields = ('product_text, product_COD') #for specific fields
        fields = '__all__'
