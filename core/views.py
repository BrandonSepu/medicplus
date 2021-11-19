from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'web/base.html')

def index(request):
    return render(request, 'web/index.html')

def tomahora(request):
    return render(request, 'web/tomahora.html')

