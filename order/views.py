from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView
from order.models import Order, ByProductOrders
from django.urls import reverse_lazy
from .services import cancel_order
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin

from product.models import Announcement


class OderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order/order_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset  # Если есть право доступа, то пользователь видит все заказы
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        now = datetime.date.today()
        bp_orders = ByProductOrders.objects.all()
        context_data['now'] = now
        context_data['bp_orders'] = bp_orders
        return context_data


@login_required
def cancel_order_func(request, pk):
    order_obj = Order.objects.filter(pk=pk).get()
    if request.method == 'POST':
        if request.user == Order.objects.filter(pk=pk).get().user:
            Order.objects.filter(pk=pk).update(status=request.POST['cancel'])
            if cancel_order(date=order_obj.date, order_quantity_hc=order_obj.half_carcasses_quantity,
                            order_obj=order_obj) is True:
                return redirect(reverse_lazy('order:order_list'))
            else:
                return redirect(reverse_lazy('order:order_list'))
        else:
            return redirect(reverse_lazy('order:home'))
    bp_orders = ByProductOrders.objects.filter(order_id=pk)
    context = {
        'object': order_obj,
        'bp_orders': bp_orders
    }
    return render(request, template_name='order/order_cancel.html', context=context)


def main_page(request):
    if Announcement.objects.count() > 0:
        announcement = Announcement.objects.all().get().body
        context = {
            "announcement": announcement,
        }
        return render(request, template_name='order/index.html', context=context)
    else:
        return render(request, template_name='order/index.html')


def contact(request):
    return render(request, template_name='order/contacts.html')


@login_required
def complete_order(request):
    order_obj = Order.objects.filter(user=request.user).last()
    bp_orders = ByProductOrders.objects.filter(order=order_obj.pk)
    context = {
        "order_obj": order_obj,
        "bp_orders": bp_orders,
    }
    return render(request, template_name='order/complete_order.html', context=context)
