import calendar
from .models import Date, ByProduct
import datetime


def create_calendar():
    name_month = {
        1: 'Январь',
        2: 'Февраль',
        3: 'Март',
        4: 'Апрель',
        5: 'Май',
        6: 'Июнь',
        7: 'Июль',
        8: 'Август',
        9: 'Сентябрь',
        10: 'Октябрь',
        11: 'Ноябрь',
        12: 'Декабрь',
    }
    name_month_two = {
        1: 'Январе',
        2: 'Феврале',
        3: 'Марте',
        4: 'Апреле',
        5: 'Мае',
        6: 'Июне',
        7: 'Июле',
        8: 'Августе',
        9: 'Сентябре',
        10: 'Октябре',
        11: 'Ноябре',
        12: 'Декабре',
    }
    year = datetime.date.today().year
    current_month = datetime.date.today().month
    next_month = current_month + 1

    first_call = calendar.monthcalendar(year=year, month=current_month)
    second_call = calendar.monthcalendar(year=year, month=next_month)

    current_month_title = name_month[current_month]
    next_month_title = name_month[next_month]

    current_month_title_two = name_month_two[current_month]
    next_month_title_two = name_month_two[next_month]

    call_list = [first_call, second_call, current_month_title, next_month_title, current_month, current_month_title_two,
                 next_month_title_two]

    return call_list


def parse_month(dict_month: dict):
    days_list = []
    date_list = []
    for week in dict_month['days']:
        for day in week:
            if day == 0:
                continue
            else:
                if day < 10:
                    days_list.append('0' + str(day))
                else:
                    days_list.append(str(day))
    month = str(dict_month['month'])
    year = str(dict_month['year'])
    for day in days_list:
        date_str_obj = f'{year}-{month}-{day}'
        date_obj = datetime.datetime.strptime(date_str_obj, '%Y-%m-%d').date()
        date_list.append(date_obj)
    return date_list


def create_multiple_date(date_list: list, half_carcasses_int, half_carcasses_quantity, bp1, bp1q, bp2, bp2q, bp3, bp3q,
                         bp4, bp4q, bp5, bp5q, bp6, bp6q, bp7, bp7q, bp8, bp8q, bp9, bp9q, bp10, bp10q, bp11, bp11q,
                         bp12, bp12q, bp13, bp13q, bp14, bp14q, bp15, bp15q, bp16, bp16q, bp17, bp17q, bp18, bp18q,
                         bp19, bp19q, bp20, bp20q):
    if ByProduct.objects.filter(pk=int(bp1)).exists():
        bp1 = ByProduct.objects.filter(pk=int(bp1)).get().pk
    if ByProduct.objects.filter(pk=int(bp2)).exists():
        bp2 = ByProduct.objects.filter(pk=int(bp2)).get().pk
    if ByProduct.objects.filter(pk=int(bp3)).exists():
        bp3 = ByProduct.objects.filter(pk=int(bp3)).get().pk
    if ByProduct.objects.filter(pk=int(bp4)).exists():
        bp4 = ByProduct.objects.filter(pk=int(bp4)).get().pk
    if ByProduct.objects.filter(pk=int(bp5)).exists():
        bp5 = ByProduct.objects.filter(pk=int(bp5)).get().pk
    if ByProduct.objects.filter(pk=int(bp6)).exists():
        bp6 = ByProduct.objects.filter(pk=int(bp6)).get().pk
    if ByProduct.objects.filter(pk=int(bp7)).exists():
        bp7 = ByProduct.objects.filter(pk=int(bp7)).get().pk
    if ByProduct.objects.filter(pk=int(bp8)).exists():
        bp8 = ByProduct.objects.filter(pk=int(bp8)).get().pk
    if ByProduct.objects.filter(pk=int(bp9)).exists():
        bp9 = ByProduct.objects.filter(pk=int(bp9)).get().pk
    if ByProduct.objects.filter(pk=int(bp10)).exists():
        bp10 = ByProduct.objects.filter(pk=int(bp10)).get().pk
    if ByProduct.objects.filter(pk=int(bp11)).exists():
        bp11 = ByProduct.objects.filter(pk=int(bp11)).get().pk
    if ByProduct.objects.filter(pk=int(bp12)).exists():
        bp12 = ByProduct.objects.filter(pk=int(bp12)).get().pk
    if ByProduct.objects.filter(pk=int(bp13)).exists():
        bp13 = ByProduct.objects.filter(pk=int(bp13)).get().pk
    if ByProduct.objects.filter(pk=int(bp14)).exists():
        bp14 = ByProduct.objects.filter(pk=int(bp14)).get().pk
    if ByProduct.objects.filter(pk=int(bp15)).exists():
        bp15 = ByProduct.objects.filter(pk=int(bp15)).get().pk
    if ByProduct.objects.filter(pk=int(bp16)).exists():
        bp16 = ByProduct.objects.filter(pk=int(bp16)).get().pk
    if ByProduct.objects.filter(pk=int(bp17)).exists():
        bp17 = ByProduct.objects.filter(pk=int(bp17)).get().pk
    if ByProduct.objects.filter(pk=int(bp18)).exists():
        bp18 = ByProduct.objects.filter(pk=int(bp18)).get().pk
    if ByProduct.objects.filter(pk=int(bp19)).exists():
        bp19 = ByProduct.objects.filter(pk=int(bp19)).get().pk
    if ByProduct.objects.filter(pk=int(bp20)).exists():
        bp20 = ByProduct.objects.filter(pk=int(bp20)).get().pk

    for d in date_list:
        if d < datetime.date.today():
            continue
        else:
            if Date.objects.filter(date=d).exists():
                continue
            else:
                date = Date.objects.create(date=d, half_carcasses_id=half_carcasses_int,
                                           half_carcasses_quantity=half_carcasses_quantity)
                if bp1q > 0:
                    date.by_product.add(bp1, through_defaults={'quantity': bp1q})
                if bp2q > 0:
                    date.by_product.add(bp2, through_defaults={'quantity': bp2q})
                if bp3q > 0:
                    date.by_product.add(bp3, through_defaults={'quantity': bp3q})
                if bp4q > 0:
                    date.by_product.add(bp4, through_defaults={'quantity': bp4q})
                if bp5q > 0:
                    date.by_product.add(bp5, through_defaults={'quantity': bp5q})
                if bp6q > 0:
                    date.by_product.add(bp6, through_defaults={'quantity': bp6q})
                if bp7q > 0:
                    date.by_product.add(bp7, through_defaults={'quantity': bp7q})
                if bp8q > 0:
                    date.by_product.add(bp8, through_defaults={'quantity': bp8q})
                if bp9q > 0:
                    date.by_product.add(bp9, through_defaults={'quantity': bp9q})
                if bp10q > 0:
                    date.by_product.add(bp10, through_defaults={'quantity': bp10q})
                if bp11q > 0:
                    date.by_product.add(bp11, through_defaults={'quantity': bp11q})
                if bp12q > 0:
                    date.by_product.add(bp12, through_defaults={'quantity': bp12q})
                if bp13q > 0:
                    date.by_product.add(bp13, through_defaults={'quantity': bp13q})
                if bp14q > 0:
                    date.by_product.add(bp14, through_defaults={'quantity': bp14q})
                if bp15q > 0:
                    date.by_product.add(bp15, through_defaults={'quantity': bp15q})
                if bp16q > 0:
                    date.by_product.add(bp16, through_defaults={'quantity': bp16q})
                if bp17q > 0:
                    date.by_product.add(bp17, through_defaults={'quantity': bp17q})
                if bp18q > 0:
                    date.by_product.add(bp18, through_defaults={'quantity': bp18q})
                if bp19q > 0:
                    date.by_product.add(bp19, through_defaults={'quantity': bp19q})
                if bp20q > 0:
                    date.by_product.add(bp20, through_defaults={'quantity': bp20q})