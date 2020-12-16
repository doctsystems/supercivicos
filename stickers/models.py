from django.db import models
from core.models import ModeloBase
from empresas.models import Empresa
from stdimage import StdImageField

class Stickers(ModeloBase):
	empresa = models.ForeignKey(Empresa, related_name='stickers', on_delete=models.CASCADE)
	nombre = models.CharField(max_length=100)
	dimensiones = models.CharField(max_length=100)
	imagen = StdImageField(upload_to='media/stickers/', null=False, blank=True)

	class Meta:
		verbose_name="Sticker"
		verbose_name_plural="Stickers"

	def __str__(self):
		return self.nombre
