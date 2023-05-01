from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    message =" <h1> Welcome to home page</h1> "
    return HttpResponse(message)
