from django.http import HttpResponse
from django.shortcuts import render

from .models import Product
from .forms import ProductForm

# Create your views here.
def product_create_view(request, *args, **kwargs):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form" : form
    }
    return render (request, 'products/product_create.html', context)


def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    # context = {
    #     "title" : obj.title,
    #     "price" : obj.price,
    #     "description" : obj.description,
    # }
    context = {
        "object" : obj
    }
    return render (request, 'products/product_details.html', context)
