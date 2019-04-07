from django.shortcuts import render
from .models import Product, ProductCategory

def main(request):
    category_list = ProductCategory.objects.all()
    product_list = Product.objects.all()
    return render(request, 'mainapp/index.html',context={'products': product_list, 'categorys': category_list})

def products(request, pk=None):
    return render(request, 'mainapp/products.html')

def contacts(request):
    return render(request, 'mainapp/contacts.html')

