from django.contrib import admin

# Register your models here.
from .models import Categoria, TipoAtuacao, Pais, Produtora, Membro, Filmes, Atuacao

admin.site.register(Categoria)
admin.site.register(TipoAtuacao)
admin.site.register(Pais)
admin.site.register(Produtora)
# admin.site.register(Membro)
# admin.site.register(Filmes)

class AtuacaoInline(admin.TabularInline):
    model = Atuacao

@admin.register(Membro)
class Membroadimin(admin.ModelAdmin):
    inlines    =[AtuacaoInline]

@admin.register(Filmes)
class Filmeadimin(admin.ModelAdmin):
    inlines    =[AtuacaoInline]