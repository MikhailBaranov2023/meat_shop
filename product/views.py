from django.shortcuts import render
from django.views import generic
from .models import Date, ByProduct, HalfCarcasses
from .forms import DateForm, HalfCarcassesForm
from django.urls import reverse_lazy


class CreateDate(generic.CreateView):
    model = Date
    form_class = DateForm
    success_url = reverse_lazy('order:home')


class DateList(generic.ListView):
    model = Date
    template_name = 'product/date_list.html'



class CreateProduct(generic.CreateView):
    model = HalfCarcasses
    form_class = HalfCarcassesForm
    template_name = 'product/halfcarses_form.html'
    success_url = reverse_lazy('product:date_add')


