from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView
from order.models import Order
from django.urls import reverse_lazy
from .services import cancel_order
import datetime
from django.http import Http404

from django.contrib.auth.mixins import LoginRequiredMixin


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
        context_data['now'] = now

        return context_data


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('order:home')

    def get_object(self, queryset=None):
        """ Проверка на то, что пользователь не может удалить чужой заказ """
        self.object = super().get_object(queryset)
        if self.object.user == self.request.user or self.request.user.is_staff:
            today = datetime.date.today()
            time_dlt = self.object.date.date - today
            if time_dlt.days <= 1:
                raise redirect(reverse_lazy('order:order_list'))
            else:
                return self.object
        elif self.object.user != self.request.user:
            raise Http404

    def form_valid(self, form):
        date_to_return = super().form_valid(form)
        if self.request.method == "POST":
            cancel_order(date=self.object.date, order_quantity_hc=self.object.half_carcasses_quantity,
                         order_quantity_bp=self.object.by_product_quantity)

        return date_to_return


@login_required
def cancel_order_func(request, pk):
    order_obj = Order.objects.filter(pk=pk).get()
    if request.method == 'POST':
        Order.objects.filter(pk=pk).update(status=request.POST['cancel'])
        cancel_order(date=order_obj.date, order_quantity_hc=order_obj.half_carcasses_quantity,
                     order_quantity_bp=order_obj.by_product_quantity)
        return redirect(reverse_lazy('order:order_list'))
    context = {
        'object': order_obj
    }
    return render(request, template_name='order/order_cancel.html', context=context)


def main_page(request):
    return render(request, template_name='order/index.html')


def contact(request):
    return render(request, template_name='order/contacts.html')
