from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from empresas.models import Direccion, Empresa, Responsable
from empresas.serializers import DireccionSerializer, EmpresaSerializer, ResponsableSerializer

class EmpresaAPIView(APIView):
	serializer_class=EmpresaSerializer
	def get(self, request, format=None):
		empresas=Empresa.objects.all()
		data=EmpresaSerializer(empresas, many=True).data
		return Response(data)

	def post(self, request, format=None):
		serializer=self.serializer_class(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DireccionAPIView(APIView):
	serializer_class=DireccionSerializer
	def get(self, request, format=None):
		dirs=Direccion.objects.all()
		data=DireccionSerializer(dirs, many=True).data
		return Response(data)

	def post(self, request, format=None):
		serializer=self.serializer_class(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResponsableAPIView(APIView):
	
	def get(self, request, format=None):
		resps=Responsable.objects.all()
		data=ResponsableSerializer(resps, many=True).data
		return Response(data)

	serializer_class=ResponsableSerializer
	def post(self, request, format=None):
		serializer=self.serializer_class(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)