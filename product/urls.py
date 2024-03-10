from django.urls import path
from .apps import ProductConfig
from .views import DateList, make_order_current_month, next_month, current_month, \
    create_date_current_month, create_date_next_month, add_current_month, add_next_month, make_order_next_month

app_name = ProductConfig.name

urlpatterns = [
    path('date_list/', DateList.as_view(), name='date_list'),
    path('detect_current_month/<int:day>/', make_order_current_month, name='detect_date_current'),
    path('detect_next_month/<int:day>/', make_order_next_month, name='detect_date_next'),
    path('next_month', next_month, name='next_month'),
    path('current_month/', current_month, name='current_month'),
    path('create_date_current_month/', create_date_current_month,
         name='create_date_current_month'),
    path('create_date_next_month/', create_date_next_month, name='create_date_next_month'),
    path('add_current_month/', add_current_month, name='add_current_month'),
    path('add_next_month/', add_next_month, name='add_next_month'),
]
