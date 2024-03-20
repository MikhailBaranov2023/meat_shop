from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Date, ByProduct, HalfCarcasses, ByProductItem
from django.urls import reverse_lazy
from product.services import create_calendar, parse_month, create_multiple_date
import datetime
import json
from order.services import create_order
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def create_date_current_month(request, date_list=[]):
    """Выбираем даты для добавления в текущем месяце"""
    calendar = create_calendar()
    half_carcasses = HalfCarcasses.objects.all()
    by_product = ByProduct.objects.all()
    if request.user.is_staff:
        if request.method == 'GET':
            date_list = []
        if request.method == 'POST':
            try:
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
                    half_carcasses_quantity = int(request.POST['half_carcasses_quantity'])
                    by_product1 = request.POST['by_product1']
                    if request.POST['by_product1_quantity'] == '':
                        by_product1_quantity = 0
                    else:
                        by_product1_quantity = int(request.POST['by_product1_quantity'])
                    by_product2 = request.POST['by_product2']
                    if request.POST['by_product2_quantity'] == '':
                        by_product2_quantity = 0
                    else:
                        by_product2_quantity = int(request.POST['by_product2_quantity'])
                    by_product3 = request.POST['by_product3']
                    if request.POST['by_product3_quantity'] == '':
                        by_product3_quantity = 0
                    else:
                        by_product3_quantity = int(request.POST['by_product3_quantity'])
                    by_product4 = request.POST['by_product4']
                    if request.POST['by_product4_quantity'] == '':
                        by_product4_quantity = 0
                    else:
                        by_product4_quantity = int(request.POST['by_product4_quantity'])
                    by_product5 = request.POST['by_product5']
                    if request.POST['by_product5_quantity'] == '':
                        by_product5_quantity = 0
                    else:
                        by_product5_quantity = int(request.POST['by_product5_quantity'])
                    by_product6 = request.POST['by_product6']
                    if request.POST['by_product6_quantity'] == '':
                        by_product6_quantity = 0
                    else:
                        by_product6_quantity = int(request.POST['by_product6_quantity'])
                    by_product7 = request.POST['by_product7']
                    if request.POST['by_product7_quantity'] == '':
                        by_product7_quantity = 0
                    else:
                        by_product7_quantity = int(request.POST['by_product7_quantity'])
                    by_product8 = request.POST['by_product8']
                    if request.POST['by_product8_quantity'] == '':
                        by_product8_quantity = 0
                    else:
                        by_product8_quantity = int(request.POST['by_product8_quantity'])
                    by_product9 = request.POST['by_product9']
                    if request.POST['by_product9_quantity'] == '':
                        by_product9_quantity = 0
                    else:
                        by_product9_quantity = int(request.POST['by_product9_quantity'])
                    by_product10 = request.POST['by_product10']
                    if request.POST['by_product10_quantity'] == '':
                        by_product10_quantity = 0
                    else:
                        by_product10_quantity = int(request.POST['by_product10_quantity'])
                    by_product11 = request.POST['by_product11']
                    if request.POST['by_product11_quantity'] == '':
                        by_product11_quantity = 0
                    else:
                        by_product11_quantity = int(request.POST['by_product11_quantity'])
                    by_product12 = request.POST['by_product12']
                    if request.POST['by_product12_quantity'] == '':
                        by_product12_quantity = 0
                    else:
                        by_product12_quantity = int(request.POST['by_product12_quantity'])
                    by_product13 = request.POST['by_product13']
                    if request.POST['by_product13_quantity'] == '':
                        by_product13_quantity = 0
                    else:
                        by_product13_quantity = int(request.POST['by_product13_quantity'])
                    by_product14 = request.POST['by_product14']
                    if request.POST['by_product14_quantity'] == '':
                        by_product14_quantity = 0
                    else:
                        by_product14_quantity = int(request.POST['by_product14_quantity'])
                    by_product15 = request.POST['by_product15']
                    if request.POST['by_product15_quantity'] == '':
                        by_product15_quantity = 0
                    else:
                        by_product15_quantity = int(request.POST['by_product15_quantity'])
                    by_product16 = request.POST['by_product16']
                    if request.POST['by_product16_quantity'] == '':
                        by_product16_quantity = 0
                    else:
                        by_product16_quantity = int(request.POST['by_product16_quantity'])
                    by_product17 = request.POST['by_product17']
                    if request.POST['by_product17_quantity'] == '':
                        by_product17_quantity = 0
                    else:
                        by_product17_quantity = int(request.POST['by_product17_quantity'])
                    by_product18 = request.POST['by_product18']
                    if request.POST['by_product18_quantity'] == '':
                        by_product18_quantity = 0
                    else:
                        by_product18_quantity = int(request.POST['by_product18_quantity'])
                    by_product19 = request.POST['by_product19']
                    if request.POST['by_product19_quantity'] == '':
                        by_product19_quantity = 0
                    else:
                        by_product19_quantity = int(request.POST['by_product19_quantity'])
                    by_product20 = request.POST['by_product20']
                    if request.POST['by_product20_quantity'] == '':
                        by_product20_quantity = 0
                    else:
                        by_product20_quantity = int(request.POST['by_product20_quantity'])
                    create_multiple_date(date_list=date_list, half_carcasses_int=half_carcasses_int,
                                         half_carcasses_quantity=half_carcasses_quantity, bp1=by_product1,
                                         bp1q=by_product1_quantity, bp2=by_product2, bp2q=by_product2_quantity,
                                         bp3=by_product3, bp3q=by_product3_quantity, bp4=by_product4,
                                         bp4q=by_product4_quantity, bp5=by_product5, bp5q=by_product5_quantity,
                                         bp6=by_product6, bp6q=by_product6_quantity, bp7=by_product7,
                                         bp7q=by_product7_quantity, bp8=by_product8, bp8q=by_product8_quantity,
                                         bp9=by_product9, bp9q=by_product9_quantity, bp10=by_product10,
                                         bp10q=by_product10_quantity, bp11=by_product11, bp11q=by_product11_quantity,
                                         bp12=by_product12, bp12q=by_product12_quantity, bp13=by_product13,
                                         bp13q=by_product13_quantity, bp14=by_product14, bp14q=by_product14_quantity,
                                         bp15=by_product15,
                                         bp15q=by_product15_quantity, bp16=by_product16, bp16q=by_product16_quantity,
                                         bp17=by_product17,
                                         bp17q=by_product17_quantity, bp18=by_product18, bp18q=by_product18_quantity,
                                         bp19=by_product19, bp19q=by_product19_quantity, bp20=by_product20,
                                         bp20q=by_product20_quantity)

                    date_list = []
            except ValueError:
                redirect(reverse_lazy('product:create_date_current_month'))
    else:
        return redirect('order:home')

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


@login_required
def create_date_next_month(request, date_list=[]):
    """Выбираем даты для добавления в слудеюзщем месяце месяце"""
    calendar = create_calendar()
    half_carcasses = HalfCarcasses.objects.all()
    by_product = ByProduct.objects.all()
    if request.user.is_staff:
        if request.method == 'GET':
            date_list = []
        if request.method == 'POST':
            try:
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
                    half_carcasses_quantity = int(request.POST['half_carcasses_quantity'])
                    by_product1 = request.POST['by_product1']
                    if request.POST['by_product1_quantity'] == '':
                        by_product1_quantity = 0
                    else:
                        by_product1_quantity = int(request.POST['by_product1_quantity'])
                    by_product2 = request.POST['by_product2']
                    if request.POST['by_product2_quantity'] == '':
                        by_product2_quantity = 0
                    else:
                        by_product2_quantity = int(request.POST['by_product2_quantity'])
                    by_product3 = request.POST['by_product3']
                    if request.POST['by_product3_quantity'] == '':
                        by_product3_quantity = 0
                    else:
                        by_product3_quantity = int(request.POST['by_product3_quantity'])
                    by_product4 = request.POST['by_product4']
                    if request.POST['by_product4_quantity'] == '':
                        by_product4_quantity = 0
                    else:
                        by_product4_quantity = int(request.POST['by_product4_quantity'])
                    by_product5 = request.POST['by_product5']
                    if request.POST['by_product5_quantity'] == '':
                        by_product5_quantity = 0
                    else:
                        by_product5_quantity = int(request.POST['by_product5_quantity'])
                    by_product6 = request.POST['by_product6']
                    if request.POST['by_product6_quantity'] == '':
                        by_product6_quantity = 0
                    else:
                        by_product6_quantity = int(request.POST['by_product6_quantity'])
                    by_product7 = request.POST['by_product7']
                    if request.POST['by_product7_quantity'] == '':
                        by_product7_quantity = 0
                    else:
                        by_product7_quantity = int(request.POST['by_product7_quantity'])
                    by_product8 = request.POST['by_product8']
                    if request.POST['by_product8_quantity'] == '':
                        by_product8_quantity = 0
                    else:
                        by_product8_quantity = int(request.POST['by_product8_quantity'])
                    by_product9 = request.POST['by_product9']
                    if request.POST['by_product9_quantity'] == '':
                        by_product9_quantity = 0
                    else:
                        by_product9_quantity = int(request.POST['by_product9_quantity'])
                    by_product10 = request.POST['by_product10']
                    if request.POST['by_product10_quantity'] == '':
                        by_product10_quantity = 0
                    else:
                        by_product10_quantity = int(request.POST['by_product10_quantity'])
                    by_product11 = request.POST['by_product11']
                    if request.POST['by_product11_quantity'] == '':
                        by_product11_quantity = 0
                    else:
                        by_product11_quantity = int(request.POST['by_product11_quantity'])
                    by_product12 = request.POST['by_product12']
                    if request.POST['by_product12_quantity'] == '':
                        by_product12_quantity = 0
                    else:
                        by_product12_quantity = int(request.POST['by_product12_quantity'])
                    by_product13 = request.POST['by_product13']
                    if request.POST['by_product13_quantity'] == '':
                        by_product13_quantity = 0
                    else:
                        by_product13_quantity = int(request.POST['by_product13_quantity'])
                    by_product14 = request.POST['by_product14']
                    if request.POST['by_product14_quantity'] == '':
                        by_product14_quantity = 0
                    else:
                        by_product14_quantity = int(request.POST['by_product14_quantity'])
                    by_product15 = request.POST['by_product15']
                    if request.POST['by_product15_quantity'] == '':
                        by_product15_quantity = 0
                    else:
                        by_product15_quantity = int(request.POST['by_product15_quantity'])
                    by_product16 = request.POST['by_product16']
                    if request.POST['by_product16_quantity'] == '':
                        by_product16_quantity = 0
                    else:
                        by_product16_quantity = int(request.POST['by_product16_quantity'])
                    by_product17 = request.POST['by_product17']
                    if request.POST['by_product17_quantity'] == '':
                        by_product17_quantity = 0
                    else:
                        by_product17_quantity = int(request.POST['by_product17_quantity'])
                    by_product18 = request.POST['by_product18']
                    if request.POST['by_product18_quantity'] == '':
                        by_product18_quantity = 0
                    else:
                        by_product18_quantity = int(request.POST['by_product18_quantity'])
                    by_product19 = request.POST['by_product19']
                    if request.POST['by_product19_quantity'] == '':
                        by_product19_quantity = 0
                    else:
                        by_product19_quantity = int(request.POST['by_product19_quantity'])
                    by_product20 = request.POST['by_product20']
                    if request.POST['by_product20_quantity'] == '':
                        by_product20_quantity = 0
                    else:
                        by_product20_quantity = int(request.POST['by_product20_quantity'])
                    create_multiple_date(date_list=date_list, half_carcasses_int=half_carcasses_int,
                                         half_carcasses_quantity=half_carcasses_quantity, bp1=by_product1,
                                         bp1q=by_product1_quantity, bp2=by_product2, bp2q=by_product2_quantity,
                                         bp3=by_product3, bp3q=by_product3_quantity, bp4=by_product4,
                                         bp4q=by_product4_quantity, bp5=by_product5, bp5q=by_product5_quantity,
                                         bp6=by_product6, bp6q=by_product6_quantity, bp7=by_product7,
                                         bp7q=by_product7_quantity, bp8=by_product8, bp8q=by_product8_quantity,
                                         bp9=by_product9, bp9q=by_product9_quantity, bp10=by_product10,
                                         bp10q=by_product10_quantity, bp11=by_product11, bp11q=by_product11_quantity,
                                         bp12=by_product12, bp12q=by_product12_quantity, bp13=by_product13,
                                         bp13q=by_product13_quantity, bp14=by_product14, bp14q=by_product14_quantity,
                                         bp15=by_product15,
                                         bp15q=by_product15_quantity, bp16=by_product16, bp16q=by_product16_quantity,
                                         bp17=by_product17,
                                         bp17q=by_product17_quantity, bp18=by_product18, bp18q=by_product18_quantity,
                                         bp19=by_product19, bp19q=by_product19_quantity, bp20=by_product20,
                                         bp20q=by_product20_quantity)

                    date_list = []
            except ValueError:
                redirect(reverse_lazy('product:create_date_current_month'))
    else:
        return redirect('order:home')

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


@login_required
def add_current_month(request):
    calendar = create_calendar()
    half_carcasses = HalfCarcasses.objects.all()
    by_product = ByProduct.objects.all()
    if request.method == 'POST':
        try:
            dict_month = json.loads(request.POST['month'])
            half_carcasses_int = request.POST['half_carcasses']
            half_carcasses_quantity = int(request.POST['half_carcasses_quantity'])
            date_list = parse_month(dict_month=dict_month)
            by_product1 = request.POST['by_product1']
            if request.POST['by_product1_quantity'] == '':
                by_product1_quantity = 0
            else:
                by_product1_quantity = int(request.POST['by_product1_quantity'])
            by_product2 = request.POST['by_product2']
            if request.POST['by_product2_quantity'] == '':
                by_product2_quantity = 0
            else:
                by_product2_quantity = int(request.POST['by_product2_quantity'])
            by_product3 = request.POST['by_product3']
            if request.POST['by_product3_quantity'] == '':
                by_product3_quantity = 0
            else:
                by_product3_quantity = int(request.POST['by_product3_quantity'])
            by_product4 = request.POST['by_product4']
            if request.POST['by_product4_quantity'] == '':
                by_product4_quantity = 0
            else:
                by_product4_quantity = int(request.POST['by_product4_quantity'])
            by_product5 = request.POST['by_product5']
            if request.POST['by_product5_quantity'] == '':
                by_product5_quantity = 0
            else:
                by_product5_quantity = int(request.POST['by_product5_quantity'])
            create_multiple_date(date_list=date_list, half_carcasses_int=half_carcasses_int,
                                 half_carcasses_quantity=half_carcasses_quantity, bp1=by_product1,
                                 bp1q=by_product1_quantity, bp2=by_product2, bp2q=by_product2_quantity, bp3=by_product3,
                                 bp3q=by_product3_quantity, bp4=by_product4, bp4q=by_product4_quantity, bp5=by_product5,
                                 bp5q=by_product5_quantity)
            return redirect(reverse_lazy('order:home'))
        except ValueError:
            redirect(reverse_lazy('product:add_current_month'))

    context = {
        'current_month': calendar[0],
        'current_month_title': calendar[2],
        'half_carcasses': half_carcasses,
        'by_product': by_product,
        'number_mount': calendar[4],
    }
    return render(request, 'product/add_month.html', context=context)


@login_required
def add_next_month(request):
    if request.user.is_staff:
        calendar = create_calendar()
        half_carcasses = HalfCarcasses.objects.all()
        by_product = ByProduct.objects.all()
        if request.method == 'POST':
            try:
                dict_month = json.loads(request.POST['month'])
                half_carcasses_int = request.POST['half_carcasses']
                half_carcasses_quantity = int(request.POST['half_carcasses_quantity'])
                by_product1 = request.POST['by_product1']
                date_list = parse_month(dict_month=dict_month)
                if request.POST['by_product1_quantity'] == '':
                    by_product1_quantity = 0
                else:
                    by_product1_quantity = int(request.POST['by_product1_quantity'])
                by_product2 = request.POST['by_product2']
                if request.POST['by_product2_quantity'] == '':
                    by_product2_quantity = 0
                else:
                    by_product2_quantity = int(request.POST['by_product2_quantity'])
                by_product3 = request.POST['by_product3']
                if request.POST['by_product3_quantity'] == '':
                    by_product3_quantity = 0
                else:
                    by_product3_quantity = int(request.POST['by_product3_quantity'])
                by_product4 = request.POST['by_product4']
                if request.POST['by_product4_quantity'] == '':
                    by_product4_quantity = 0
                else:
                    by_product4_quantity = int(request.POST['by_product4_quantity'])
                by_product5 = request.POST['by_product5']
                if request.POST['by_product5_quantity'] == '':
                    by_product5_quantity = 0
                else:
                    by_product5_quantity = int(request.POST['by_product5_quantity'])
                create_multiple_date(date_list=date_list, half_carcasses_int=half_carcasses_int,
                                     half_carcasses_quantity=half_carcasses_quantity, bp1=by_product1,
                                     bp1q=by_product1_quantity, bp2=by_product2, bp2q=by_product2_quantity,
                                     bp3=by_product3,
                                     bp3q=by_product3_quantity, bp4=by_product4, bp4q=by_product4_quantity,
                                     bp5=by_product5,
                                     bp5q=by_product5_quantity)
                return redirect(reverse_lazy('order:home'))
            except ValueError:
                redirect(reverse_lazy('product:add_next_month'))

        context = {
            'next_month': calendar[1],
            'next_month_title': calendar[3],
            'number_mount': calendar[4] + 1,
            'half_carcasses': half_carcasses,
            'by_product': by_product,
        }
        return render(request, 'product/add_month.html', context=context)
    else:
        return redirect('order:home')


class DateList(LoginRequiredMixin, generic.ListView):
    model = Date
    template_name = 'product/date_list.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        calendar = create_calendar()
        context_data['current_month'] = calendar[0]
        context_data['current_month_title'] = calendar[2]
        context_data['number_mount'] = calendar[4]
        return context_data


@login_required
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


@login_required
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


@login_required
def make_order_current_month(request, day):
    if request.method == 'POST':
        all_keys = request.POST.keys()
        static_keys = ['csrfmiddlewaretoken', 'half_carcasses_quantity', 'description', 'date']
        bp_keys = []
        bp_value = []
        for key in all_keys:
            if key in static_keys:
                continue
            else:
                bp_keys.append(key)
        for quant in request.POST.keys():
            for k in bp_keys:
                if quant == k:
                    bp_value.append(request.POST[quant])
                else:
                    continue
        bp_dict = dict(zip(bp_keys, bp_value))
        try:
            date_id = int(request.POST['date'])
            half_carcasses_quantity = int(request.POST['half_carcasses_quantity'])
            description = request.POST['description']
            user = request.user
            if create_order(date_int=date_id, order_quantity_hc=half_carcasses_quantity,
                            description=description, user=user, bp_dict=bp_dict) is True:
                return redirect(reverse_lazy('order:complete_order'))
            else:
                return redirect(reverse_lazy('order:order_is_not_created'))
        except ValueError:
            redirect(reverse_lazy('order:order_is_not_created'))
    # date_item = get_object_or_404(Date, pk=pk)
    date_all = Date.objects.all()
    calendar = create_calendar()
    if day >= 10:
        if calendar[4] > 10:
            detect_date = f"{datetime.date.today().year}-{calendar[4]}-{day}"
            date_time_obj = datetime.datetime.strptime(detect_date, '%Y-%m-%d')
            if Date.objects.filter(date=date_time_obj.date()).exists():
                date_item = get_object_or_404(Date, date=date_time_obj.date())
                by_product_items = ByProductItem.objects.filter(date_id=date_item.pk)
                context = {
                    'object': date_item,
                    'object_list': date_all,
                    'current_month': calendar[0],
                    'current_month_title': calendar[2],
                    'number_mount': calendar[4],
                    'by_product_items': by_product_items,
                }
                return render(request, template_name='product/date_list.html',
                              context=context)
            else:
                return redirect(reverse_lazy('product:current_month'))
        else:
            detect_date = f"{datetime.date.today().year}-0{calendar[4]}-{day}"
            date_time_obj = datetime.datetime.strptime(detect_date, '%Y-%m-%d')
            if Date.objects.filter(date=date_time_obj.date()).exists():
                date_item = get_object_or_404(Date, date=date_time_obj.date())
                by_product_items = ByProductItem.objects.filter(date_id=date_item.pk)
                context = {
                    'object': date_item,
                    'object_list': date_all,
                    'current_month': calendar[0],
                    'current_month_title': calendar[2],
                    'number_mount': calendar[4],
                    'by_product_items': by_product_items,
                }
                return render(request, template_name='product/date_list.html',
                              context=context)
            else:
                return redirect(reverse_lazy('product:current_month'))
    else:
        if calendar[4] >= 10:
            detect_date = f"{datetime.date.today().year}-{calendar[4]}-0{day}"
            date_time_obj = datetime.datetime.strptime(detect_date, '%Y-%m-%d')
            if Date.objects.filter(date=date_time_obj.date()).exists():
                date_item = get_object_or_404(Date, date=date_time_obj.date())
                by_product_items = ByProductItem.objects.filter(date_id=date_item.pk)
                context = {
                    'object': date_item,
                    'object_list': date_all,
                    'current_month': calendar[0],
                    'current_month_title': calendar[2],
                    'number_mount': calendar[4],
                    'by_product_items': by_product_items,
                }
                return render(request, template_name='product/date_list.html',
                              context=context)
            else:
                return redirect(reverse_lazy('product:current_month'))
        else:
            detect_date = f"{datetime.date.today().year}-0{calendar[4]}-0{day}"
            date_time_obj = datetime.datetime.strptime(detect_date, '%Y-%m-%d')
            if Date.objects.filter(date=date_time_obj.date()).exists():
                date_item = get_object_or_404(Date, date=date_time_obj.date())
                by_product_items = ByProductItem.objects.filter(date_id=date_item.pk)
                context = {
                    'object': date_item,
                    'object_list': date_all,
                    'current_month': calendar[0],
                    'current_month_title': calendar[2],
                    'number_mount': calendar[4],
                    'by_product_items': by_product_items,
                }
                return render(request, template_name='product/date_list.html',
                              context=context)
            else:
                return redirect(reverse_lazy('product:current_month'))


@login_required
def make_order_next_month(request, day):
    if request.method == 'POST':
        all_keys = request.POST.keys()
        static_keys = ['csrfmiddlewaretoken', 'half_carcasses_quantity', 'description', 'date']
        bp_keys = []
        bp_value = []
        for key in all_keys:
            if key in static_keys:
                continue
            else:
                bp_keys.append(key)
        for quant in request.POST.keys():
            for k in bp_keys:
                if quant == k:
                    bp_value.append(request.POST[quant])
                else:
                    continue
        bp_dict = dict(zip(bp_keys, bp_value))
        try:
            date_id = int(request.POST['date'])
            half_carcasses_quantity = int(request.POST['half_carcasses_quantity'])
            description = request.POST['description']
            user = request.user
            if create_order(date_int=date_id, order_quantity_hc=half_carcasses_quantity,
                            description=description, user=user, bp_dict=bp_dict) is True:
                return redirect(reverse_lazy('order:complete_order'))
            else:
                return redirect(reverse_lazy('order:order_is_not_created'))
        except ValueError:
            redirect(reverse_lazy('order:order_is_not_created'))

    date_all = Date.objects.all()
    calendar = create_calendar()
    number_mount = calendar[4] + 1
    if day >= 10:
        if number_mount >= 10:
            detect_date = f"{datetime.date.today().year}-{number_mount}-{day}"
            date_time_obj = datetime.datetime.strptime(detect_date, '%Y-%m-%d')
            if Date.objects.filter(date=date_time_obj.date()).exists():
                date_item = get_object_or_404(Date, date=date_time_obj.date())
                by_product_items = ByProductItem.objects.filter(date_id=date_item.pk)
                context = {
                    'object': date_item,
                    'object_list': date_all,
                    'next_month': calendar[1],
                    'next_month_title': calendar[3],
                    'number_mount': number_mount,
                    'by_product_items': by_product_items,

                }
                return render(request, template_name='product/date_list.html',
                              context=context)
            else:
                return redirect(reverse_lazy('product:next_month'))
        else:
            detect_date = f"{datetime.date.today().year}-0{number_mount}-{day}"
            date_time_obj = datetime.datetime.strptime(detect_date, '%Y-%m-%d')
            if Date.objects.filter(date=date_time_obj.date()).exists():
                date_item = get_object_or_404(Date, date=date_time_obj.date())
                by_product_items = ByProductItem.objects.filter(date_id=date_item.pk)
                context = {
                    'object': date_item,
                    'object_list': date_all,
                    'next_month': calendar[1],
                    'next_month_title': calendar[3],
                    'number_mount': number_mount,
                    'by_product_items': by_product_items,

                }
                return render(request, template_name='product/date_list.html',
                              context=context)
            else:
                return redirect(reverse_lazy('product:next_month'))
    else:
        if number_mount >= 10:
            detect_date = f"{datetime.date.today().year}-{number_mount}-0{day}"
            date_time_obj = datetime.datetime.strptime(detect_date, '%Y-%m-%d')
            if Date.objects.filter(date=date_time_obj.date()).exists():
                date_item = get_object_or_404(Date, date=date_time_obj.date())
                by_product_items = ByProductItem.objects.filter(date_id=date_item.pk)
                context = {
                    'object': date_item,
                    'object_list': date_all,
                    'next_month': calendar[1],
                    'next_month_title': calendar[3],
                    'number_mount': number_mount,
                    'by_product_items': by_product_items,

                }
                return render(request, template_name='product/date_list.html',
                              context=context)
            else:
                return redirect(reverse_lazy('product:next_month'))
        else:
            detect_date = f"{datetime.date.today().year}-0{number_mount}-0{day}"
            date_time_obj = datetime.datetime.strptime(detect_date, '%Y-%m-%d')
            if Date.objects.filter(date=date_time_obj.date()).exists():
                date_item = get_object_or_404(Date, date=date_time_obj.date())
                by_product_items = ByProductItem.objects.filter(date_id=date_item.pk)
                context = {
                    'object': date_item,
                    'object_list': date_all,
                    'next_month': calendar[1],
                    'next_month_title': calendar[3],
                    'number_mount': number_mount,
                    'by_product_items': by_product_items,

                }
                return render(request, template_name='product/date_list.html',
                              context=context)
            else:
                return redirect(reverse_lazy('product:next_month'))
