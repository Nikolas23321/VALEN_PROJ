from django.contrib import admin
from .models import Casa, Categoria, Objetivo

# Register your models here.

@admin.register(Casa)
class CasaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'titulo', 'localizacao', 'hospedes', 'quartos', 'categoria', 'em_destaque')
    search_fields = ('titulo', 'localizacao')
    list_filter = ('categoria', 'em_destaque')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)


@admin.register(Objetivo)
class ObjetivoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'titulo', 'ordem')
    search_fields = ('titulo',)
