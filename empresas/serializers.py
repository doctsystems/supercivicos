from rest_framework import serializers
from empresas.models import Empresa, Responsable, Direccion

class ResponsableSerializer(serializers.ModelSerializer):

	class Meta:
		model=Responsable
		fields='__all__'

class DireccionSerializer(serializers.ModelSerializer):

	class Meta:
		model=Direccion
		fields='__all__'

	# def create(self, validated_data):
	# 	direccion=Direccion(calle=validated_data.get("calle"))
	# 	direccion.save()
	# 	return validated_data

class EmpresaSerializer(serializers.ModelSerializer):
	# direccion=serializers.StringRelatedField()
	# responsables = ResponsableSerializer(many=True)

	direcciones = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	responsables = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model=Empresa
		fields='__all__'

	# def create(self, validated_data):
	# 	empresa=Empresa(nombre=validated_data.get("nombre"))
	# 	empresa.save()
	# 	responsables=validated_data.get('responsables')
	# 	for responsable in responsables:
	# 		Responsable.objects.create(empresa=empresa, **responsable)
	# 	return validated_data
