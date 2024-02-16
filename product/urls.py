from django.urls import path
from .apps import ProductConfig
from .views import CreateDate, CreateProduct, DateList, detect_date, next_month, current_month

app_name = ProductConfig.name

urlpatterns = [
    path('add_date/', CreateDate.as_view(), name='date_add'),
    path('add_product/', CreateProduct.as_view(), name='product_add'),
    path('date_list/', DateList.as_view(), name='date_list'),
    path('detect/<int:pk>/', detect_date, name='detect_date'),
    path('next_month', next_month, name='next_month'),
    path('current_mont/', current_month, name='current_month'),
]
