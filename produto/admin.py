from django.contrib import admin
from . import models

# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao_curta', 'get_preco_fromatado']

admin.site.register(models.Produto, ProdutoAdmin)
