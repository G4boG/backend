from .models import Organizacion
from django.contrib import admin

class OrganizacionAdmin(admin.ModelAdmin):
    #titulo de las columnas
    list_display = ("nombre","tipo", "direccion", "contacto", "descripcion")
    #buscador por nombre
    search_fields = ("nombre",)
    
admin.site.register(Organizacion, OrganizacionAdmin)