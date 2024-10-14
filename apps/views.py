from django.shortcuts import render, get_object_or_404

from apps.models import Product


# Create your views here.

def index(request):
    products = Product.objects.all()  # Fetch all products with images
    return render(request, 'index.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})