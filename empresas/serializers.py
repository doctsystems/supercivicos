from rest_framework import serializers
from empresas.models import Empresa

class HelloSerializer(serializers.Serializer):
	name=serializers.CharField(max_length=10)

class EmpresaSerializer(serializers.Serializer):
	class Meta:
		model=Empresa
		fields='__all__'