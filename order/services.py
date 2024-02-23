from product.models import Date
from .models import Order
import datetime


def create_order(date_int: int, order_quantity_hc: int,
                 order_quantity_bp: int, description, user):
    date_hc_quantity = Date.objects.filter(pk=date_int).get().half_carcasses_quantity
    date_bp_quantity = Date.objects.filter(pk=date_int).get().by_product_quantity
    if order_quantity_hc <= date_hc_quantity:
        if order_quantity_bp <= date_bp_quantity:
            Order.objects.create(date_id=date_int, half_carcasses_quantity=order_quantity_hc,
                                 by_product_quantity=order_quantity_bp, description=description, user=user)
            new_hc = date_hc_quantity - order_quantity_hc
            new_bp = date_bp_quantity - order_quantity_bp
            Date.objects.filter(pk=date_int).update(half_carcasses_quantity=new_hc)
            Date.objects.filter(pk=date_int).update(by_product_quantity=new_bp)
            return True
        return False
    return False


def cancel_order(date: Date, order_quantity_hc: Order.half_carcasses_quantity,
                 order_quantity_bp: Order.by_product_quantity):
    date.half_carcasses_quantity = date.half_carcasses_quantity + order_quantity_hc
    date.by_product_quantity = date.by_product_quantity + order_quantity_bp
    date.save()
