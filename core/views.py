from django.shortcuts import render
from .models import Casa, Objetivo

# Create your views here.

def inicio(request):
    casas_destaque = Casa.objects.filter(em_destaque=True)
    objetivos = Objetivo.objects.all()

    quantidade_casas = Casa.objects.count()
    maior_capacidade = 0

    for casa in Casa.objects.all():
        if casa.hospedes > maior_capacidade:
            maior_capacidade = casa.hospedes

    return render(request, 'core/home.html', {
        'casas_destaque': casas_destaque,
        'objetivos': objetivos,
        'quantidade_casas': quantidade_casas,
        'maior_capacidade': maior_capacidade
    })

def casas(request):
    todas_as_casas = Casa.objects.all()
    return render(request, 'core/casas.html', {'casas': todas_as_casas})

def sobre(request):
    objetivos = Objetivo.objects.all()
    return render(request, 'core/sobre.html', {
        'objetivos': objetivos
    })