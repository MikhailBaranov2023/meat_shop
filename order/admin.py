from django.contrib import admin
from order.models import Order, ByProductOrders


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('half_carcasses_quantity', 'date', 'status', 'user',)
    list_filter = ('user', 'date', 'status',)
    filter_horizontal = ['by_product', ]
