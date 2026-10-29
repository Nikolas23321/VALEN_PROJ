from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'core/home.html')

def casas(request):
    return render(request, 'core/casas.html')

def sobre(request):
    return render(request, 'core/sobre.html')