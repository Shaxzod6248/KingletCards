from .serializers import *
from products.models import *
from users.models import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.generics import RetrieveAPIView


class RetrieveApiView(RetrieveAPIView):
    serializer_class = ProductRetrieveSerializer
    queryset = Products.objects.all()

    def get_object(self, *args, **kwargs):
        product = super().get_object(*args, **kwargs)
        variants = Variants.objects.filter(variants_id=product.id)
        product.variants = variants
        return product


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['^title']
    ordering_fields = ['id', 'title']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class BordersViewSet(viewsets.ModelViewSet):
    queryset = Border.objects.all()
    serializer_class = BorderSerializer


class ColorsViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class TestimonialsViewSet(viewsets.ModelViewSet):
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsSerializer


class GetUpdateViewSet(viewsets.ModelViewSet):
    queryset = GetUpdate.objects.all()
    serializer_class = GetUpdateSerializer


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class VariantsViewSet(viewsets.ModelViewSet):
    queryset = Variants.objects.all()
    serializer_class = VariantsSerializer