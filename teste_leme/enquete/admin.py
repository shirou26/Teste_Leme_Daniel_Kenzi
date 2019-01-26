from django.contrib import admin
from .models import opcoes,Pergunta,Titulo

# Register your models here.

class Opcoes_alinhadas(admin.TabularInline):
    model = opcoes
    extra = 2

class Pergunta_admin(admin.ModelAdmin):
    fieldsets = [
        (None,  {'fields': ['pergunta','imagens']})
        
    ]
    inlines = [Opcoes_alinhadas]
    list_display = ('pergunta',)
    search_filter = ['pergunta']


admin.site.register(Pergunta, Pergunta_admin)
admin.site.register(Titulo)



