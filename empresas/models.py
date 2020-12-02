from django.db import models
from core.models import ModeloBase
from stdimage import StdImageField

class Empresa(ModeloBase):
	tipos=(
		('nn', '----------'),
		('pri', 'Empresa Privada'),
		('gob', 'Institucion de Gobierno'),
	)
	tipo_de_empresa = models.CharField(max_length=3, choices=tipos, default='nn')
	nombre=models.CharField(max_length=30, unique=True)
	email=models.EmailField(max_length=50, unique=True)
	telefono=models.CharField(max_length=10)
	password=models.CharField(max_length=80)
	logo=StdImageField(upload_to='empresas/logo/',
		variations={'thumbnail': {"width": 240, "height": 200, "crop": True}},
		null=True, blank=True)
	# logo=models.ImageField(upload_to='empresas/logo64/', null=True, blank=True)
	is_verified = models.BooleanField(default=False)
	
	class Meta:
		ordering = ['-id']
		verbose_name_plural = "Empresas"

	def __str__(self):
		return '{}'.format(self.nombre)

	def save(self, *args, **kwargs):
		self.nombre=self.nombre.upper()
		super(Empresa, self).save(*args, **kwargs)

class Responsable(ModeloBase):
	empresa=models.ForeignKey(Empresa, related_name='responsables', on_delete=models.CASCADE)
	nombres=models.CharField(max_length=50)
	apellidos=models.CharField(max_length=50)
	telefono=models.CharField(max_length=10)

	class Meta:
		ordering = ['apellidos']
		verbose_name_plural="Responsables"

	def __str__(self):
		return '{} {}'.format(self.nombres, self.apellidos)

	def save(self, *args, **kwargs):
		self.nombres=self.nombres.upper()
		self.apellidos=self.apellidos.upper()
		super(Responsable, self).save(*args, **kwargs)

class Direccion(ModeloBase):
	empresa=models.ForeignKey(Empresa, related_name='direcciones', on_delete=models.CASCADE)
	calle=models.CharField(max_length=50)
	numero_exterior=models.CharField(max_length=10)
	numero_interior=models.CharField(max_length=10)
	colonia=models.CharField(max_length=30)
	ciudad=models.CharField(max_length=20)
	pais=models.CharField(max_length=20)
	codigo_postal=models.CharField(max_length=50)

	class Meta:
		verbose_name_plural="Direcciones"

	def __str__(self):
		return '{}, {}, {}'.format(self.calle, self.ciudad, self.pais)

	def save(self, *args, **kwargs):
		self.calle=self.calle.upper()
		self.colonia=self.colonia.upper()
		self.ciudad=self.ciudad.upper()
		self.pais=self.pais.upper()
		super(Direccion, self).save(*args, **kwargs)
