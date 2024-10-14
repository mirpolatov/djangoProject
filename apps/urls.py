from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),  # This maps the root URL to the index view
]
