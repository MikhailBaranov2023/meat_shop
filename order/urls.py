from django.urls import path
from .apps import OrderConfig
from .views import OderListView, OrderCreateView, OrderDeleteView, main_page, contact

app_name = OrderConfig.name

urlpatterns = [
    path('', main_page, name='home'),
    path('list/', OderListView.as_view(), name='order_list'),
    path('create/<int:pk>/', OrderCreateView.as_view(), name='order_create'),
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),
    path('contact/', contact, name='contact'),
]
