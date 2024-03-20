from product.models import Date, ByProductItem
from .models import Order, ByProduct, ByProductOrders
import datetime


def api_create_requests(pk: Order.pk):
    order = Order.objects.filter(pk=pk).get()
    by_products = ByProductOrders.objects.filter(order_id=pk)
    """дата заказа"""
    date = order.date
    print(f'дата-{date.date}')
    """id полутуши и количество"""
    half_carcasses_id = order.date.half_carcasses.pk
    half_carcasses_price = order.date.half_carcasses.price
    half_carcasses_quantity = order.half_carcasses_quantity
    print(f'полутуша:id-{half_carcasses_id} - {half_carcasses_price}р/шт - {half_carcasses_quantity}шт')
    """id субпродуктов и их количество и название и цена """
    for bp in by_products:
        by_product_id = bp.by_product.pk
        bp_product_title = bp.by_product.title
        bp_product_price = bp.by_product.price
        by_product_quantity = bp.quantity
        if bp.by_product.kg is True:
            by_product_type_price = 'кг'
        else:
            by_product_type_price = 'шт'
        print(
            f'{by_product_id}-{bp_product_title}-{bp_product_price}-{by_product_quantity}-{by_product_type_price}')
    "описание заказа"
    description = order.description
    print(f'описание заказа{description}')
    "заказчик"
    phone = order.user.phone
    first_name = order.user.first_name
    last_name = order.user.last_name
    print(f'заказчик{phone}-{first_name}-{last_name}')


def create_order(date_int: int, order_quantity_hc: int, description, user, bp_dict: dict):
    date_now = datetime.date.today()
    date_hc_quantity = Date.objects.filter(pk=date_int).get().half_carcasses_quantity
    date_obj = Date.objects.filter(pk=date_int).get().date
    time_delta = date_obj - date_now
    cancel_date = date_obj - datetime.timedelta(days=1)
    if time_delta.days >= 0:
        if order_quantity_hc <= date_hc_quantity:

            if Order.objects.filter(user=user, date_id=date_int, status='accepted').exists():
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
                            print(by_product)
                            order.by_product.add(by_product, through_defaults={'quantity': int(bp_dict[k])})
                            byproduct_item_quantity = ByProductItem.objects.filter(date_id=order.date.pk,
                                                                                   by_product=by_product).get().quantity
                            if byproduct_item_quantity < int(bp_dict[k]):
                                date_hc_quantity_after_order = Date.objects.filter(
                                    pk=date_int).get().half_carcasses_quantity
                                cancel_hc_quantity = date_hc_quantity_after_order + order_quantity_hc
                                Date.objects.filter(pk=date_int).update(half_carcasses_quantity=cancel_hc_quantity)
                                order.delete()
                                return False
                            else:
                                new_quant = byproduct_item_quantity - int(bp_dict[k])
                                ByProductItem.objects.filter(date_id=order.date.pk, by_product=by_product).update(
                                    quantity=new_quant)
                        else:
                            continue
                """вот тут будет выполняться функция, передается order.pk"""
                # api_create_requests(order.pk)
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
