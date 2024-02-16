from product.models import Date
from .models import Order
import datetime


def create_order(date: Date, order_quantity_hc: Order.half_carcasses_quantity,
                 order_quantity_bp: Order.by_product_quantity):
    date.half_carcasses_quantity = date.half_carcasses_quantity - order_quantity_hc
    date.by_product_quantity = date.by_product_quantity - order_quantity_bp
    date.save()


def cancel_order(date: Date, order_quantity_hc: Order.half_carcasses_quantity,
                 order_quantity_bp: Order.by_product_quantity):
    date.half_carcasses_quantity = date.half_carcasses_quantity + (order_quantity_hc)
    date.by_product_quantity = date.by_product_quantity + (order_quantity_bp)

    date.save()
