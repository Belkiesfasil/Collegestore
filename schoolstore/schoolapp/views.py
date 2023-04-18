from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Stream, Product


# Create your views here.
# def index(request):
#     return HttpResponse("Hey am here")

# def home(request):
#     return render(request,"home.html")
def allStream(request,c_slug=None):
    c_page=None
    products_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Stream,slug=c_slug)
        products_list = Product.objects.all().filter(stream=c_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
    paginator = Paginator(products_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, "stream.html", {'stream': c_page, 'products': products})

def prodDetail(request,c_slug,product_slug):
    try:
        product=Product.objects.get(stream__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e

    return render(request,'product.html',{'product':product})


