from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
import random
from basketapp.models import Basket


def main(request):
    product_list = Product.objects.all()

    return render(request, 'mainapp/index.html', context={'user': request.user , 'products': product_list})


def get_hot_product():
    return Product.objects.all().order_by('?').first()

def get_hot_product_from_admin():
    hot_products = Product.objects.all(is_hot=True)
    if hot_products:
        hot_product = hot_products[0]
    else:
        hot_product = Product.objects.first()
    return hot_product

def get_some_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category). \
                        exclude(pk=hot_product.pk)[:3]

    return same_products

def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    basket = request.user.basket.all()
    if pk:
        if pk =='0':
            category = {'name':'Все'}
            product_list = Product.objects.all()
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            product_list = Product.objects.filter(category=category.id)
        context = {
            'title': 'родукты',
            'links_menu': links_menu,
            'products': product_list,
            'category': category,
            'basket': basket
        }
        return render(request, 'mainapp/product_list.html', context)
    else:
        product_list = Product.objects.all()
        hot_product = get_hot_product()
        same_products = get_some_products(hot_product)
        context = {
            'title': 'родукты',
            'links_menu': links_menu,
            'hot_product': hot_product,
            'same_products': same_products
    }

    return render(request, 'mainapp/products.html', context)

def product(request, pk):
    links_menu = ProductCategory.objects.all()
    title = 'Продукт'
    basket = request.user.basket.all()

    context = {
        'title': title,
        'links_menu': links_menu,
        'product': get_object_or_404(Product, pk=pk),
        'basket': basket,
    }
    return render(request, 'mainapp/product.html', context)

def contacts(request):
    return render(request, 'mainapp/contacts.html')