from django.urls import path
from .views import index, product_detail

urlpatterns = [
    path('menu/', index, name='index'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
]

