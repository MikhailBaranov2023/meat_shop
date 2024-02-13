from django.urls import path
from .apps import OrderConfig
from .views import OderListView, OrderCreateView, OrderDeleteView

app_name = OrderConfig.name

urlpatterns = [
    path('', OderListView.as_view(), name='home'),
    path('create/<int:pk>/', OrderCreateView.as_view(), name='order_create'),
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),
]
