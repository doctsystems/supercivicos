from rest_framework import serializers
from empresas.models import Empresa, Responsable, Direccion
from django.core.validators import FileExtensionValidator

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
	password = serializers.CharField(max_length=80, min_length=6, write_only=True)
	logo = serializers.ImageField(
		validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], 
		required=False
	)

	class Meta:
		model=Empresa
		fields='__all__'
		read_only_fields = ['estado', 'is_verified',]

class EmailVerificationSerializer(serializers.ModelSerializer):
	token = serializers.CharField(max_length=555)

	class Meta:
		model = Empresa
		fields = ['token']