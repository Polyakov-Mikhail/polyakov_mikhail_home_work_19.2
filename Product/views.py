from django.shortcuts import render, get_object_or_404

from Product.models import Product


def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products_list.html', context)


def product_detail(request, pk):
    product_name = get_object_or_404(Product, pk=pk)
    context = {'product': product_name}
    return render(request, 'product_detail.html', context)
