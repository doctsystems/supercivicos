from django.db import models

class Categoria(models.Model):
    nombre=models.CharField(max_length=100, unique=True)
    descricpcion=models.TextField()

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"


    def __str__(self):
        return self.nombre
