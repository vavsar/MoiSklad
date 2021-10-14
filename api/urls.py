from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import GetBrandSalesView, WareViewSet, SaleViewSet

router_v1 = DefaultRouter()
router_v1.register('wares', WareViewSet, basename='wares')
router_v1.register('sales', SaleViewSet, basename='sales')
router_v1.register('get_brand_sales', GetBrandSalesView, basename='get_brand_sales')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
