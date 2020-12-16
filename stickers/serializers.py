from rest_framework import serializers
from empresas.models import Empresa
from .models import Stickers
from drf_base64.fields import Base64ImageField
from empresas.serializers import EmpresaSerializer

class StickersSerializer(serializers.ModelSerializer):
	imagen = Base64ImageField(required=False)
	empresa = EmpresaSerializer(read_only=True)
	empresaid = serializers.PrimaryKeyRelatedField(write_only=True, queryset = Empresa.objects.all(), source = 'empresa')

	class Meta:
		model = Stickers
		# fields = '__all__'
		read_only_fields = ['estado', ]
		exclude = ['estado', 'fecha_creacion', 'fecha_modificacion', 'usuario_creacion', 'usuario_modificacion']
