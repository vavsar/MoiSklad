from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import GetBrandSales

router_v1 = DefaultRouter()

urlpatterns = [
    path('v1/get_brand_sales/', GetBrandSales.as_vies(), name='get_brand_sales'),
    path('v1/', include(router_v1.urls)),
]
