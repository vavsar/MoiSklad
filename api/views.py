from django.db.models import Count, Sum, F
from django_filters.rest_framework import DjangoFilterBackend
from psycopg2._psycopg import Float
from rest_framework import viewsets

from .models import Ware, Sale
from .serializers import GetBrandSalesSerializer, WareSerializer, SaleSerializer


class WareViewSet(viewsets.ModelViewSet):
    queryset = Ware.objects.all()
    serializer_class = WareSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class GetBrandSalesView(viewsets.ModelViewSet):
    total_sold = Sum('sales__quantity')
    queryset = Ware.objects.annotate(
        total_sold=total_sold
    ).annotate(
        total_earned=F('price') * total_sold,
    )
    serializer_class = GetBrandSalesSerializer
    filter_backends = [DjangoFilterBackend, ]
    # filterset_fields = ['brand', ]
