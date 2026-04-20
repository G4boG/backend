from django.contrib import admin
from django.urls import path
import socios.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', views.hola_mundo),
    path('main/', views.main),
    path('organizacion/<str:nombre>/', views.detalle_organizacion, name='detalle_org'),
]

