from django.shortcuts import render

from Product.models import Product


def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products_list.html', context)
