from rest_framework import serializers
from empresas.models import Empresa, Responsable, Direccion

class HelloSerializer(serializers.Serializer):
	name=serializers.CharField(max_length=10)

class ResponsableSerializer(serializers.ModelSerializer):
	class Meta:
		model=Responsable
		fields=['nombres', 'apellidos', 'celular']

class DireccionSerializer(serializers.ModelSerializer):
	class Meta:
		model=Direccion
		fields='__all__'

class EmpresaSerializer(serializers.ModelSerializer):
	# responsables=serializers.StringRelatedField(many=True)
	# direccion=serializers.StringRelatedField()
	
	responsables = ResponsableSerializer(many=True, read_only=True)
	direccion = DireccionSerializer(read_only=True)

	class Meta:
		model=Empresa
		fields=['id', 'nombre', 'email', 'telefono', 'direccion', 'responsables']

	def create(self, validated_data):
		responsables_data = validated_data.pop('responsables')
		empresa = Empresa.objects.create(**validated_data)
		for responsable in responsables:
			Responsable.objects.create(empresa=empresa, **responsable)
		return empresa
