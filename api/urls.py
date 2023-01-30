from django.conf import settings
from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



router = DefaultRouter()
router.register('Category', CategoryViewSet)
router.register('Products', ProductsViewSet)
router.register('Orders', OrdersViewSet)
router.register('Colors', ColorsViewSet)
router.register('Borders', BordersViewSet)
router.register('Comments', TestimonialsViewSet)
router.register('GetUpdate', GetUpdateViewSet)
router.register('ContactUs', ContactUsViewSet)
router.register('Variants', VariantsViewSet)
router.register('Checkout_form', CheckoutViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('Retrieve/Products/<int:pk>/', RetrieveApiView.as_view()),
]