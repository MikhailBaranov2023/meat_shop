import calendar
import datetime


def create_calendar():
    name_month = {
        1: 'Январь',
        2: 'Февраль',
        3: 'Март',
        4: 'Апрель',
        5: 'Март',
        6: 'Июнь',
        7: 'Июль',
        8: 'Август',
        9: 'Сентябрь',
        10: 'Октябрь',
        11: 'Ноябрь',
        12: 'Декабрь',
    }
    year = datetime.date.today().year
    current_month = datetime.date.today().month
    next_month = current_month + 1

    first_call = calendar.monthcalendar(year=year, month=current_month)
    second_call = calendar.monthcalendar(year=year, month=next_month)

    current_month_title = name_month[current_month]
    next_month_title = name_month[next_month]

    call_list = [first_call, second_call, current_month_title, next_month_title, current_month]

    return call_list
