from rest_framework import serializers
from empresas.models import Empresa, Responsable, Direccion
from django.core.validators import FileExtensionValidator
from drf_base64.fields import Base64ImageField

class ResponsableSerializer(serializers.ModelSerializer):

	class Meta:
		model=Responsable
		fields='__all__'

class DireccionSerializer(serializers.ModelSerializer):

	class Meta:
		model=Direccion
		fields='__all__'

class EmpresaSerializer(serializers.ModelSerializer):
	direcciones = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	responsables = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	# password = serializers.CharField(max_length=80, min_length=6, write_only=True)
	logo=Base64ImageField(required=False)

	class Meta:
		model=Empresa
		# fields = '__all__'
		read_only_fields = ['estado', ]
		exclude = ['estado', 'fecha_creacion', 'fecha_modificacion', 'usuario_creacion', 'usuario_modificacion']

class EmailVerificationSerializer(serializers.ModelSerializer):
	token = serializers.CharField(max_length=555)

	class Meta:
		model = Empresa
		fields = ['token']