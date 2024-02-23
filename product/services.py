import calendar
from .models import Date
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


def create_multiple_date(date_list: list, half_carcasses_int, by_product_int, half_carcasses_quantity,
                         by_product_quantity):
    for d in date_list:
        if d < datetime.date.today():
            continue
        else:
            if Date.objects.filter(date=d).exists():
                continue
            else:
                Date.objects.create(date=d, half_carcasses_id=half_carcasses_int, by_product_id=by_product_int,
                                    half_carcasses_quantity=half_carcasses_quantity,
                                    by_product_quantity=by_product_quantity)
