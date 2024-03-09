from product.models import Date, ByProductItem
from .models import Order, ByProduct, ByProductOrders
import datetime


def create_order(date_int: int, order_quantity_hc: int, description, user, bp_dict: dict):
    date_now = datetime.date.today()
    date_hc_quantity = Date.objects.filter(pk=date_int).get().half_carcasses_quantity
    date_obj = Date.objects.filter(pk=date_int).get().date
    time_delta = date_obj - date_now
    cancel_date = date_obj - datetime.timedelta(days=1)
    if time_delta.days >= 0:
        if order_quantity_hc <= date_hc_quantity:

            if Order.objects.filter(user=user, date_id=date_int).exists():
                return False
            else:
                order = Order.objects.create(date_id=date_int, half_carcasses_quantity=order_quantity_hc,
                                             description=description, user=user,
                                             cancel_date=cancel_date)
                new_hc = date_hc_quantity - order_quantity_hc
                Date.objects.filter(pk=date_int).update(half_carcasses_quantity=new_hc)
                for k in bp_dict.keys():
                    if bp_dict[k] == '':
                        continue
                    else:
                        if int(bp_dict[k]) > 0:
                            by_product = ByProduct.objects.filter(title=k).get().pk
                            order.by_product.add(by_product, through_defaults={'quantity': int(bp_dict[k])})
                            byproduct_item_quantity = ByProductItem.objects.filter(date_id=order.date.pk,
                                                                                   by_product=by_product).get().quantity
                            new_quant = byproduct_item_quantity - int(bp_dict[k])
                            ByProductItem.objects.filter(date_id=order.date.pk, by_product=by_product).update(
                                quantity=new_quant)
                        else:
                            continue
                    """сюда внедрять api frontpad"""
                    date = order.date.date
                    user = order.user_id
                    """полутуши"""
                    half_carcasses = order.date.half_carcasses
                    half_carcasses_quantity = order.half_carcasses_quantity
                    """субпродукты"""
                    for bp in order.by_product:
                        by_product_id = bp.pk
                        bp_quantity = bp.quantity

                return True

        return False
    else:
        return False


def cancel_order(date: Date, order_quantity_hc: Order.half_carcasses_quantity, order_obj: Order):
    date.half_carcasses_quantity = date.half_carcasses_quantity + order_quantity_hc
    date.save()
    bp_items = ByProductOrders.objects.filter(order=order_obj.pk)
    bp_list = []
    quant_list = []
    for b in bp_items:
        bp_list.append(b.by_product.title)
        quant_list.append(b.quantity)
    bp_dict = dict(zip(bp_list, quant_list))
    for k in bp_dict.keys():
        by_product = ByProduct.objects.filter(title=k).get().pk
        byproduct_item_quantity = ByProductItem.objects.filter(date_id=order_obj.date.pk,
                                                               by_product=by_product).get().quantity
        new_quant = byproduct_item_quantity + int(bp_dict[k])
        ByProductItem.objects.filter(date_id=order_obj.date.pk, by_product=by_product).update(
            quantity=new_quant)
    return True
