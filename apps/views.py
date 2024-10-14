from django.shortcuts import render

from apps.models import Product


# Create your views here.

def index(request):
    products = Product.objects.all()  # Fetch all products with images
    return render(request, 'index.html', {'products': products})