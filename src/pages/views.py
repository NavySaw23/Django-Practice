from django.http import HttpResponse #makes the html functional
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request)
    print(request.user)    #request.user is used for authentication and stuff
    print(args)
    print(kwargs)
    #above 3 lines show what request is being made
    return HttpResponse("<h1> Hello world </h1>") 

def contact_view(*args, **kwargs):
    return HttpResponse("<h1> Contacts page </h1>") 

def template_view(request, *args, **kwargs):
    return render(request, "template.html", {})

