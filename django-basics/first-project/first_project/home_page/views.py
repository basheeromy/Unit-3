from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Products

products = Products.objects.all()

# Create your views here.


def home_view(request):
    if 'username' in request.session:
        product = {
            'products' : products
        }
        return render(request,'home_page/index.html',product)
    return redirect('login_page')