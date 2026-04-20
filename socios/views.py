from django.shortcuts import render
from django.http import HttpResponse
from .models import Organizacion  

def hola_mundo(request):
    return render(request, 'principal/index.html')

def main(request):
    
    lista_orgs = [
        Organizacion(nombre='Juan', tipo='Fundación', direccion='Calle Falsa 123', contacto='123456789', descripcion='Prueba 1'),
        Organizacion(nombre='Maria', tipo='Junta de Vecinos', direccion='Avenida 456', contacto='987654321', descripcion='Prueba 2'),
        Organizacion(nombre='Pedro', tipo='Club Deportivo', direccion='Boulevard 789', contacto='555555555', descripcion='Prueba 3'),
    ]

    
    datos = {
        'organizaciones': lista_orgs
    }
    return render(request, 'principal/index.html', datos)
    


def detalle_organizacion(request, nombre):
    lista_orgs = [
        Organizacion(nombre='Juan', tipo='Fundación', direccion='Calle Falsa 123', contacto='123456789', descripcion='Prueba 1'),
        Organizacion(nombre='Maria', tipo='Junta de Vecinos', direccion='Avenida 456', contacto='987654321', descripcion='Prueba 2'),
        Organizacion(nombre='Pedro', tipo='Club Deportivo', direccion='Boulevard 789', contacto='555555555', descripcion='Prueba 3'),
    ]
    for org in lista_orgs:
        if org.nombre == nombre:
            socio_encontrado = org
            break
    

    a = {
        'org': socio_encontrado
    }
    
    return render(request, 'principal/detalle_organizacion.html', a)



    