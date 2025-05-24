from django.shortcuts import render
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def contacts(request):
    return render(request, 'contacts.html')


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'catalog/product_detail.html', {'product': product})
