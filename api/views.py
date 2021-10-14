from itertools import chain

from django.db.models import Sum, F, Subquery, OuterRef
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Ware, Sale, Order
from .serializers import (GetBrandSalesSerializer, WareSerializer,
                          SaleSerializer, OrderSerializer, )


class WareViewSet(viewsets.ModelViewSet):
    queryset = Ware.objects.all()
    serializer_class = WareSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class GetBrandSalesView(viewsets.ModelViewSet):
    serializer_class = GetBrandSalesSerializer
    filter_backends = [DjangoFilterBackend, ]
    # filterset_fields = ['brand', ]

    def get_queryset(self):
        queryset = Ware.objects.annotate(
            total_sold=Subquery(
                Sale.objects.filter(
                    supplierArticle=OuterRef('pk')
                ).values(
                    'supplierArticle'
                ).annotate(
                    sold=Sum('quantity'),
                ).values('sold')[:1]
            ),
            total_ordered=Sum('orders__quantity'),
        ).annotate(
            total_earned=Subquery(
                Sale.objects.filter(
                    supplierArticle=OuterRef('pk')
                ).values(
                    'supplierArticle'
                ).annotate(
                    earned=F('supplierArticle__price') * Sum('quantity'),
                ).values('earned')[:1]
            ),
            orders_earned=F('price') * Sum('orders__quantity'),
        )
        return queryset

    # def get_queryset(self):
    #     total_sold = Sum('sales__quantity')
    #     total_ordered = Sum('orders__quantity')
    #     queryset1 = Ware.objects.annotate(
    #         total_sold=total_sold,
    #     ).annotate(
    #         total_earned=F('price') * total_sold
    #     )
    #     queryset2 = Ware.objects.annotate(
    #         total_ordered=total_ordered,
    #     ).annotate(
    #         orders_earned=F('price') * total_ordered
    #     )
    #     qs = list(chain(queryset1, queryset2))
    #     for asdf in queryset1:
    #         print(asdf.total_sold)
    #     return qs
