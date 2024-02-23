from django.urls import path
from .apps import ProductConfig
from .views import CreateProduct, DateList, make_order, next_month, current_month, \
    create_date_current_month, create_date_next_month, add_current_month, add_next_month

app_name = ProductConfig.name

urlpatterns = [
    path('add_product/', CreateProduct.as_view(), name='product_add'),
    path('date_list/', DateList.as_view(), name='date_list'),
    path('detect/<int:pk>/', make_order, name='detect_date'),
    path('next_month', next_month, name='next_month'),
    path('current_month/', current_month, name='current_month'),
    path('create_date_current_month/', create_date_current_month,
         name='create_date_current_month'),
    path('create_date_next_month/', create_date_next_month, name='create_date_next_month'),
    path('add_current_month/', add_current_month, name='add_current_month'),
    path('add_next_month/', add_next_month, name='add_next_month'),
]
