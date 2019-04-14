from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory


def main(request):
    product_list = Product.objects.all()

    return render(request, 'mainapp/index.html', context={'user': request.user , 'products': product_list})


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

    else:
        product_list = Product.objects.all()
        context = {
            'title': 'родукты',
            'links_menu': links_menu,
            'products': product_list,
            'basket': basket

    }

    return render(request, 'mainapp/product_list.html', context)

def contacts(request):
    return render(request, 'mainapp/contacts.html')