from django.urls import path
from .apps import ProductConfig
from .views import CreateDate, CreateProduct, DateList

app_name = ProductConfig.name

urlpatterns = [
    path('add_date/', CreateDate.as_view(), name='date_add'),
    path('add_product/', CreateProduct.as_view(), name='product_add'),
    path('date_list/', DateList.as_view(), name='date_list'),
]
