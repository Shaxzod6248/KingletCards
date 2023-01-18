from rest_framework import serializers
from products.models import *
from users.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class BorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Border
        fields = '__all__'