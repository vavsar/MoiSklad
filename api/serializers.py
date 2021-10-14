from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from .models import Ware, Sale, Order


class WareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ware
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

    def create(self, validated_data):
        instance = Sale.objects.create(**validated_data)
        sale_quantity = validated_data['quantity']
        supplier_article = validated_data['supplierArticle']
        discountPercent = validated_data['discountPercent']
        ware = get_object_or_404(Ware, pk=supplier_article.id)
        if ware.quantity < sale_quantity:
            raise ValidationError('quantity is not enough')
        ware.quantity -= sale_quantity
        ware.save()
        instance.totalPrice = (
            ware.price * sale_quantity) - (
                (ware.price * sale_quantity) / 100 * discountPercent
        )
        instance.save()
        # instance.priceWithDisc = (
        #         instance.totalPrice * ((100 - instance.discountPercent) / 100) *
        #         ((100 - instance.promoCodeDiscount) / 100) *
        #         ((100 - instance.spp) / 100)
        # )
        # instance.finishedPrice = (
        #         instance.totalPrice * (
        #             (100 - instance.discountPercent) / 100) *
        #         ((100 - instance.promoCodeDiscount) / 100) *
        #         ((100 - instance.spp) / 100)
        # )
        # instance.forPay = instance.priceWithDisc / 100 * 80
        # instance.save()
        return instance


class GetBrandSalesSerializer(serializers.ModelSerializer):
    total_sold = serializers.IntegerField(read_only=True)
    total_earned = serializers.FloatField(read_only=True)
    total_ordered = serializers.IntegerField(read_only=True)
    orders_earned = serializers.IntegerField(read_only=True)

    class Meta:
        model = Ware
        fields = (
            'id', 'name', 'quantity', 'price', 'total_sold',
            'total_earned', 'total_ordered', 'orders_earned'
        )
