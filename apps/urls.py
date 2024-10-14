from django.urls import path
from .views import index, product_detail

urlpatterns = [
    path('', index, name='index'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
]

