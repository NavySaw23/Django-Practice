from django.http import HttpResponse
from django.shortcuts import render

from .models import Product

# Create your views here.
def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    context = {
        "title" : obj.title,
        "price" : obj.price,
        "description" : obj.description,
    }
    return render (request, 'products/details.html', context)
