from django.db import models
from core.models import ModeloBase

class Direccion(ModeloBase):
	calle=models.CharField(max_length=50)
	numero_exterior=models.CharField(max_length=10)
	numero_interior=models.CharField(max_length=10)
	colonia=models.CharField(max_length=30, unique=True)
	ciudad=models.CharField(max_length=20, unique=True)
	pais=models.CharField(max_length=20, unique=True)
	cp=models.CharField(max_length=50)

	class Meta:
		verbose_name_plural="Direcciones"

	def __str__(self):
		return '{}, {}, {}'.format(self.calle, self.ciudad, self.pais)

	def save(self):
		self.calle=self.calle.upper()
		self.colonia=self.colonia.upper()
		self.ciudad=self.ciudad.upper()
		self.pais=self.pais.upper()
		super(Direccion, self).save()

class Empresa(ModeloBase):
	nombre=models.CharField(max_length=30, unique=True)
	email=models.EmailField(max_length=50, unique=True)
	telefono=models.CharField(max_length=10)
	contrasenia=models.CharField(max_length=50)
	direccion=models.OneToOneField(Direccion, related_name='direccion', on_delete=models.CASCADE)

	class Meta:
		ordering = ['nombre']
		verbose_name = "Empresa"
		verbose_name_plural = "Empresas"

	def __str__(self):
		return '{}'.format(self.nombre)

	def save(self):
		self.nombre=self.nombre.upper()
		super(Empresa, self).save()

class Responsable(ModeloBase):
	empresa=models.ForeignKey(Empresa, related_name='responsables', on_delete=models.CASCADE)
	nombres=models.CharField(max_length=50)
	apellidos=models.CharField(max_length=10)
	celular=models.CharField(max_length=10)

	class Meta:
		ordering = ['apellidos']
		verbose_name_plural="Responsables"

	def __str__(self):
		return '{} {}'.format(self.nombres, self.apellidos)

	def save(self):
		self.nombres=self.nombres.upper()
		self.apellidos=self.apellidos.upper()
		super(Responsable, self).save()
