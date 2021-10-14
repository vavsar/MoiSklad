from django.contrib import admin

from .models import Ware, Sale, Order


class WareAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'quantity',
        'price'
    )


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'supplierArticle',
        'quantity',
        'totalPrice',
    )


class SaleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'supplierArticle',
        'quantity',
        'totalPrice',
        'priceWithDisc'
    )

    # def supplierArticle(self, obj):
    #     return obj.wares.all()


admin.site.register(Ware, WareAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Sale, SaleAdmin)
