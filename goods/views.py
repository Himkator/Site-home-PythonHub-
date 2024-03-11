from django.shortcuts import get_list_or_404, render

from goods.models import *

# Create your views here.
def catalog(request, category_slug):
    if category_slug=='all':
        goods=Products.objects.all()
    else:
        goods=get_list_or_404(Products.objects.filter(category__slug=category_slug))
            

    context={
        'title':'Home-каталог',
        'goods':goods
    }
    return render(request, 'goods/catalog.html', context)

def product(request, slug):
    good=Products.objects.get(slug=slug)
    context={
        'good':good
    }
    return render(request, 'goods/product.html', context)