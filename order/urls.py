from django.urls import path
from django.views.decorators.cache import cache_page

from .apps import OrderConfig
from .views import OderListView, OrderDeleteView, main_page, contact, cancel_order_func, complete_order

app_name = OrderConfig.name

urlpatterns = [
    path('', main_page, name='home'),
    path('list/', OderListView.as_view(), name='order_list'),
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),
    path('contact/', contact, name='contact'),
    path('cancel_order/<int:pk>/', cancel_order_func, name='cancel_order'),
    path('copmlete_order/', complete_order, name='complete_order'),
]
