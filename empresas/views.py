from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from empresas.models import Empresa
from empresas.serializers import HelloSerializer, EmpresaSerializer

class HelloAPIView(APIView):
	serializer_class=HelloSerializer
	def get(self, request, format=None):
		an_apiview=[
			'Usamos metodos HTTP como funciones (get, post, patch, put, delete)',
			'Es similar a una View tradicional de Django',
		]
		return Response({'msj': 'HelloAPIView', 'an_apiview': an_apiview})

	def post(self, request):
		serializer=self.serializer_class(data=request.data)

		if serializer.is_valid():
			name=serializer.validated_data.get('name')
			message=f'Hello {name}'
			return Response({'msj': message})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk=None):
		return Response({'method': 'PUT'})

	def patch(self, request, pk=None):
		return Response({'method': 'PATCH'})

	def delete(self, request, pk=None):
		return Response({'method': 'DELETE'})

class EmpresaAPIView(APIView):
	# def get(self, request):
	# 	empresas=Empresa.objects.all()
	# 	data=EmpresaSerializer(empresas, many=True).data
	# 	return Response(data)
	def get(self, request, format=None):
		empresas=Empresa.objects.all()
		data=EmpresaSerializer(empresas, many=True).data
		return Response(data)
