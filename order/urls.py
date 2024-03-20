from django.urls import path
from django.views.decorators.cache import cache_page

from .apps import OrderConfig
from .views import OderListView, main_page, contact, cancel_order_func, complete_order, order_is_not_created

app_name = OrderConfig.name

urlpatterns = [
    path('', main_page, name='home'),
    path('list/', OderListView.as_view(), name='order_list'),
    path('contact/', contact, name='contact'),
    path('cancel_order/<int:pk>/', cancel_order_func, name='cancel_order'),
    path('copmlete_order/', complete_order, name='complete_order'),
    path('order_is_not_created/', order_is_not_created, name='order_is_not_created'),
]
