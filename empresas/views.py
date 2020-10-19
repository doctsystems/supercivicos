from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from empresas.models import *
from empresas.serializers import *

class apiOverview(APIView):

	def get(self, request, format=None):
		api_urls = {
			'Api':'/api/',
			'Empresas':'/api/empresas',
			'Direcciones':'/api/direcciones/',
			'Responsables':'/api/responsables/',
		}
		return Response(api_urls)

class EmpresaAPIView(APIView):

	def get(self, request, format=None):
		empresas=Empresa.objects.all()
		data=EmpresaSerializer(empresas, many=True).data
		return Response(data)

	def post(self, request, format=None):
		serializer=EmpresaSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DireccionAPIView(APIView):
	
	def get(self, request, format=None):
		dirs=Direccion.objects.all()
		data=DireccionSerializer(dirs, many=True).data
		return Response(data)

	def post(self, request, format=None):
		serializer=DireccionSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResponsableAPIView(APIView):
	
	def get(self, request, format=None):
		resps=Responsable.objects.all()
		data=ResponsableSerializer(resps, many=True).data
		return Response(data)

	def post(self, request, format=None):
		serializer=ResponsableSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.decorators import api_view
@api_view(['GET'])
def EmpresaList(request):
	empresas = Empresa.objects.all()
	serializer = EmpresaSerializer(empresas, many=True).data

	return Response(serializer)

@api_view(['POST'])
def EmpresaCreate(request):
	serializer = EmpresaSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)