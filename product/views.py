from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Date, ByProduct, HalfCarcasses
from .forms import HalfCarcassesForm
from django.urls import reverse_lazy
from product.services import create_calendar, parse_month, create_multiple_date
import datetime
from django.core.exceptions import ValidationError
import json
from order.models import Order
from order.services import create_order


def create_date_current_month(request, date_list=[]):
    """Выбираем даты для добавления в текущем месяце"""
    calendar = create_calendar()
    half_carcasses = HalfCarcasses.objects.all()
    by_product = ByProduct.objects.all()
    if request.method == 'POST':
        if 'date' in request.POST.keys():
            str_date = request.POST['date']
            date_time_obj = datetime.datetime.strptime(str_date, '%Y-%m-%d')
            date = date_time_obj.date()
            if date in date_list:
                date_list.remove(date)
            else:
                date_list.append(date)
        elif 'confirm' in request.POST.keys():
            date_list = date_list
            half_carcasses_int = request.POST['half_carcasses']
            by_product_int = request.POST['by_product']
            half_carcasses_quantity = int(request.POST['half_carcasses_quantity'])
            ValidationError('Введите число')
            by_product_quantity = int(request.POST['by_product_quantity'])
            create_multiple_date(date_list=date_list, half_carcasses_int=half_carcasses_int,
                                 by_product_int=by_product_int, half_carcasses_quantity=half_carcasses_quantity,
                                 by_product_quantity=by_product_quantity)
    else:
        date_list = []

    context = {
        'current_month': calendar[0],
        'current_month_title': calendar[2],
        'number_mount': calendar[4],
        'current_month_title_two': calendar[5],
        'date_list': date_list,
        'half_carcasses': half_carcasses,
        'by_product': by_product,
    }

    return render(request, 'product/add_date.html', context=context)


def create_date_next_month(request, date_list=[]):
    """Выбираем даты для добавления в слудеюзщем месяце месяце"""
    calendar = create_calendar()
    half_carcasses = HalfCarcasses.objects.all()
    by_product = ByProduct.objects.all()
    if request.method == 'POST':
        if 'date' in request.POST.keys():
            str_date = request.POST['date']
            date_time_obj = datetime.datetime.strptime(str_date, '%Y-%m-%d')
            date = date_time_obj.date()
            if date in date_list:
                date_list.remove(date)
            else:
                date_list.append(date)
        elif 'confirm' in request.POST.keys():
            date_list = date_list
            half_carcasses_int = request.POST['half_carcasses']
            by_product_int = request.POST['by_product']
            half_carcasses_quantity = int(request.POST['half_carcasses_quantity'])
            ValidationError('Введите число')
            by_product_quantity = int(request.POST['by_product_quantity'])
            create_multiple_date(date_list=date_list, half_carcasses_int=half_carcasses_int,
                                 by_product_int=by_product_int, half_carcasses_quantity=half_carcasses_quantity,
                                 by_product_quantity=by_product_quantity)
            date_list = []
    else:
        date_list = []
    context = {
        'next_month': calendar[1],
        'next_month_title': calendar[3],
        'number_mount': calendar[4] + 1,
        'next_month_title_two': calendar[6],
        'date_list': date_list,
        'half_carcasses': half_carcasses,
        'by_product': by_product,
    }

    return render(request, 'product/add_date.html', context=context)


def add_current_month(request):
    calendar = create_calendar()
    half_carcasses = HalfCarcasses.objects.all()
    by_product = ByProduct.objects.all()
    if request.method == 'POST':
        dict_month = json.loads(request.POST['month'])
        half_carcasses_int = request.POST['half_carcasses']
        by_product_int = request.POST['by_product']
        half_carcasses_quantity = int(request.POST['half_carcasses_quantity'])
        by_product_quantity = int(request.POST['by_product_quantity'])
        date_list = parse_month(dict_month=dict_month)
        create_multiple_date(date_list=date_list, half_carcasses_int=half_carcasses_int,
                             by_product_int=by_product_int, half_carcasses_quantity=half_carcasses_quantity,
                             by_product_quantity=by_product_quantity)

    context = {
        'current_month': calendar[0],
        'current_month_title': calendar[2],
        'half_carcasses': half_carcasses,
        'by_product': by_product,
        'number_mount': calendar[4],
    }
    return render(request, 'product/add_month.html', context=context)


def add_next_month(request):
    calendar = create_calendar()
    half_carcasses = HalfCarcasses.objects.all()
    by_product = ByProduct.objects.all()
    if request.method == 'POST':
        dict_month = json.loads(request.POST['month'])
        half_carcasses_int = request.POST['half_carcasses']
        by_product_int = request.POST['by_product']
        half_carcasses_quantity = int(request.POST['half_carcasses_quantity'])
        by_product_quantity = int(request.POST['by_product_quantity'])
        date_list = parse_month(dict_month=dict_month)
        create_multiple_date(date_list=date_list, half_carcasses_int=half_carcasses_int,
                             by_product_int=by_product_int, half_carcasses_quantity=half_carcasses_quantity,
                             by_product_quantity=by_product_quantity)

    context = {
        'next_month': calendar[1],
        'next_month_title': calendar[3],
        'number_mount': calendar[4] + 1,
        'half_carcasses': half_carcasses,
        'by_product': by_product,
    }
    return render(request, 'product/add_month.html', context=context)


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


def make_order(request, pk):
    if request.method == 'POST':
        date_id = int(request.POST['date'])
        half_carcasses_quantity = int(request.POST['half_carcasses_quantity'])
        by_product_quantity = int(request.POST['by_product_quantity'])
        description = request.POST['description']
        user = request.user
        create_order(date_int=date_id, order_quantity_hc=half_carcasses_quantity, order_quantity_bp=by_product_quantity, description=description, user=user)
        print('Заказ сформирован')

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
