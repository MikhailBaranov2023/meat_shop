from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Date, ByProduct, HalfCarcasses
from .forms import DateForm, HalfCarcassesForm
from django.urls import reverse_lazy
from product.services import create_calendar
from django.shortcuts import redirect


class CreateDate(generic.CreateView):
    model = Date
    form_class = DateForm
    success_url = reverse_lazy('order:home')
    template_name = 'product/administration.html'


class DateDetailView(generic.DetailView):
    model = Date


class DateList(generic.ListView):
    model = Date
    template_name = 'product/date_list.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        calendar = create_calendar()
        context_data['current_month'] = calendar[0]
        context_data['current_month_title'] = calendar[2]
        context_data['number_mount'] = calendar[4]
        return context_data


class CreateProduct(generic.CreateView):
    model = HalfCarcasses
    form_class = HalfCarcassesForm
    template_name = 'product/halfcarses_form.html'
    success_url = reverse_lazy('product:date_add')


def detect_date(request, pk):
    date_item = get_object_or_404(Date, pk=pk)
    date_all = Date.objects.all()
    calendar = create_calendar()
    context = {
        'object': date_item,
        'object_list': date_all,
        'current_month': calendar[0],
        'next_month': calendar[1],
        'current_month_title': calendar[2],
        'next_month_title': calendar[3],
        'number_mount': calendar[4]

    }
    return render(request, template_name='product/date_list.html', context=context)


def next_month(request):
    date = Date.objects.all()
    calendar = create_calendar()
    context = {
        'object_list': date,
        'next_month': calendar[1],
        'next_month_title': calendar[3],
        'number_mount': calendar[4] + 1,

    }
    return render(request, 'product/date_list.html', context)


def current_month(request):
    date = Date.objects.all()
    calendar = create_calendar()
    context = {
        'object_list': date,
        'current_month': calendar[0],
        'current_month_title': calendar[2],
        'number_mount': calendar[4],

    }
    return render(request, 'product/date_list.html', context, )


def add_norm_to_day(requests):
    calendar = create_calendar()
    half_carcasses = HalfCarcasses.objects.all()
    by_product = ByProduct.objects.all()

    context = {
        'current_month': calendar[0],
        'current_month_title': calendar[2],
        'half_carcasses': half_carcasses,
        'by_product': by_product,
    }
    return render(requests, template_name='product/day_norm.html', context=context)


def add_norm_to_day_next_month(request):
    calendar = create_calendar()
    context = {
        'next_month': calendar[1],
        'next_month_title': calendar[3],
    }
    return render(request, template_name='product/day_norm.html', context=context)
