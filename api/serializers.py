from rest_framework import serializers
from products.models import *
from users.models import *
from checkout.models import Checkout_form


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
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


class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = '__all__'


class GetUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetUpdate
        fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'


class VariantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variants
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class ProductRetrieveSerializer(serializers.ModelSerializer):
    variants = VariantsSerializer(many=True)

    class Meta:
        model = Products
        fields = '__all__'


class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout_form
        fields = '__all__'