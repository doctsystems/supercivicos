from rest_framework import serializers
from empresas.models import Empresa, Responsable, Direccion

class ResponsableSerializer(serializers.ModelSerializer):

	class Meta:
		model=Responsable
		fields='__all__'

	def create(self, validated_data):
		responsable=Responsable(nombre=validated_data.get("nombres"))
		responsable.save()
		return validated_data

class DireccionSerializer(serializers.ModelSerializer):

	class Meta:
		model=Direccion
		fields='__all__'

	def create(self, validated_data):
		direccion=Direccion(nombre=validated_data.get("calle"))
		direccion.save()
		return validated_data

class EmpresaSerializer(serializers.ModelSerializer):
	direccion=serializers.StringRelatedField()
	responsables = ResponsableSerializer(many=True, read_only=True)

	class Meta:
		model=Empresa
		fields='__all__'

	def create(self, validated_data):
		empresa=Empresa(nombre=validated_data.get("nombre"))
		empresa.save()
		direccion=validated_data.get('direccion')
		Direccion.objects.create(empresa=empresa, **direccion)
		responsables=validated_data.get('responsables')
		for responsable in responsables:
			Responsable.objects.create(empresa=empresa, **responsable)
		return validated_data
