from django.shortcuts import render

from goods.models import *

# Create your views here.
def catalog(request):
    goods=Products.objects.all()

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