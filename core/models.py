from django.db import models
from django_userforeignkey.models.fields import UserForeignKey

class ModeloBase(models.Model):
	estado = models.BooleanField(default=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)
	usuario_creacion = UserForeignKey(auto_user_add=True, related_name='+')
	usuario_modificacion = UserForeignKey(auto_user=True, related_name='+')

	class Meta:
		abstract=True
