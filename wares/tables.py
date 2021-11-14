import django_tables2 as tables
from django.db.models import F
from django.utils.html import format_html

from .models import Sale


class ImageColumn(tables.Column):
    def render(self, value):
        return format_html('<img src="">', value)

    def __str__(self):
        return 'Фото'


class SalesTable(tables.Table):
    photo = tables.Column(ImageColumn, empty_values=())
    color = tables.Column('Цвет', empty_values=())
    rating = tables.Column('Рейтинг', empty_values=())
    orders_quantity = tables.Column('Количество заказов', empty_values=())
    review_quantity = tables.Column('Количество отзывов', empty_values=())
    spp = tables.Column()
    order_sum = tables.Column('Сумма заказов', empty_values=())
    order_grafik = tables.Column('График заказов', empty_values=())
    quantity = tables.Column()
    sale_sum = tables.Column('Сумма продаж', empty_values=())
    sale_grafik = tables.Column('График продаж', empty_values=())

    class Meta:
        model = Sale
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            "saleID", "photo", "nmId", "category", "subject", "barcode",
            "color", "techSize", "orders_quantity", "rating", "review_quantity",
            "totalPrice", "spp", "order_sum", "order_grafik", "quantity",
            "sale_sum", "sale_grafik"
                  )

    def render_sale_sum(self, record):
        return record.quantity * record.totalPrice

    def order_sale_sum(self, queryset, is_descending):
        queryset = queryset.annotate(
            sale_sum=(F("quantity")+F("totalPrice"))
        ).order_by(("-" if is_descending else "") + "sale_sum")
        return queryset, True

    def order_photo(self, queryset, is_descending):
        return queryset, True

    def order_color(self, queryset, is_descending):
        return queryset, True

    def order_orders_quantity(self, queryset, is_descending):
        return queryset, True

    def order_rating(self, queryset, is_descending):
        return queryset, True

    def order_review_quantity(self, queryset, is_descending):
        return queryset, True

    def order_order_sum(self, queryset, is_descending):
        return queryset, True

    def order_order_grafik(self, queryset, is_descending):
        return queryset, True

    def order_sale_grafik(self, queryset, is_descending):
        return queryset, True

