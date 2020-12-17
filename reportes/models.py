from django.db import models
from core.models import ModeloBase
from django.contrib.gis.db import models as models_gis
from videos.models import Video
from django.contrib.auth.models import User

class Categoria(ModeloBase):
	nombre = models.CharField(default='cat_reporte', max_length=50, unique=True)
	is_removed = models.BooleanField(default=False)

	class Meta:
		ordering = ['-id']
		verbose_name_plural = "Categorias"

	def __str__(self):
		return '{}'.format(self.nombre)

class Reporte(ModeloBase):
	categoria = models.ForeignKey(Categoria, related_name='categorias', on_delete=models.CASCADE)
	video = models.FileField(upload_to="reportes/videos/", blank=True, null=True)
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	descripcion = models.CharField(max_length=500)
	location = models_gis.PointField(srid=4326)
	is_reported = models.BooleanField(default=True)
	is_solved = models.BooleanField(default=False)
	is_removed = models.BooleanField(default=False)

	class Meta:
		ordering = ['-id']
		verbose_name_plural = "Reportes"

	def __str__(self):
		return '{}'.format(self.descripcion)[:50]
