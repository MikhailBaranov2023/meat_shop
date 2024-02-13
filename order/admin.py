from django.contrib import admin
from order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('half_carcasses_quantity', 'by_product_quantity', 'date', 'status', 'user',)
