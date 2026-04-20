from django.db import models


class Organizacion(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, choices=[
    ('Fundación', 'Fundación'),
    ('Junta de Vecinos', 'Junta de Vecinos'),
    ('Club Deportivo', 'Club Deportivo')
])
    direccion = models.CharField(max_length=200)
    contacto = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
