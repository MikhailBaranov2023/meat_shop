from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from order.models import Order
from order.forms import OrderForm
from django.urls import reverse_lazy
from .services import create_order, cancel_order
from django.http import Http404
from product.models import Date
import datetime
from django.forms import ValidationError


class OderListView(ListView):
    model = Order
    template_name = 'order/index.html'


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('order:home')

    def form_valid(self, form, **kwargs):
        self.object = form.save()
        self.object.date = Date.objects.filter(pk=self.kwargs['pk']).get()
        self.object.user = self.request.user
        create_order(self.object.date, self.object.half_carcasses_quantity, self.object.by_product_quantity)
        self.object.save()
        return super().form_valid(form)


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('order:home')

    def get_object(self, queryset=None):
        """ Проверка на то, что пользователь не может удалить чужой заказ """
        self.object = super().get_object(queryset)
        if self.object.user == self.request.user or self.request.user.is_staff:
            return self.object
        elif self.object.user != self.request.user:
            raise Http404


def form_valid(self, form):
    cancel_order(self.object.date, self.object.half_carcasses_quantity, self.object.by_product_quantity)
    return super().form_valid(form)
