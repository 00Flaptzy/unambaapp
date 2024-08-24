from django.contrib import admin
from .models.categoria import categoria
# Register your models here.
class categoriaAdmin(admin.ModelAdmin):
    """docstring for categoriaAdmin"""
    list_display=("nombre","codigo","estado")
admin.site.register(categoria,categoriaAdmin)