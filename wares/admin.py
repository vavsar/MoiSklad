from django.contrib import admin

from .models import Sale, Order


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


admin.site.register(Order, OrderAdmin)
admin.site.register(Sale, SaleAdmin)
