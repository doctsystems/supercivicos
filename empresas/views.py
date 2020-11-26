from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from empresas.models import *
from empresas.serializers import *
from empresas.utils import *

class ApiHome(APIView):

	def get(self, request, format=None):
		api_urls = {
			'Api':'/api/',
			'Empresas':'/api/empresas',
			'Direcciones':'/api/direcciones/',
			'Responsables':'/api/responsables/',
			'Registro de Empresas':'/api/registro-empresas/',
			'Verificacion de email':'/api/verificar-email/',
		}
		return Response(api_urls)

class EmpresaAPIView(APIView):

	def get(self, request, format=None):
		empresas=Empresa.objects.all()
		data=EmpresaSerializer(empresas, many=True).data
		return Response(data)

	# def post(self, request, format=None):
	# 	serializer=EmpresaSerializer(data=request.data)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return Response(serializer.data, status=status.HTTP_201_CREATED)
	# 	else:
	# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
		responsables=Responsable.objects.all()
		data=ResponsableSerializer(responsables, many=True).data
		return Response(data)

	def post(self, request, format=None):
		serializer=ResponsableSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.hashers import make_password
from django.http import QueryDict

class RegistroEmpresaView(APIView):
	serializer_class = EmpresaSerializer

	def post(self, request):
		# print('****************')
		# print(request.data)
		qdict = QueryDict('', mutable=True)
		qdict.update(request.data)
		# print('****************')
		# print(qdict['password'])

		# request.data._mutable = True
		# request.data['password'] = make_password(request.data['password'])
		# request.data._mutable = False

		qdict['password'] = make_password(qdict['password'])
		print('****************')
		print(qdict)

		# empresa = request.data
		empresa = qdict
		serializer = self.serializer_class(data=empresa)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		empresa_data = serializer.data
		empresa = Empresa.objects.get(email=empresa_data['email'])
		token = RefreshToken.for_user(empresa).access_token
		current_site = get_current_site(request).domain
		relativeLink = reverse('empresas:verificar-email')
		absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
		email_body = 'Hi '+empresa.nombre + \
		    ' Use the link below to verify your email \n' + absurl
		data = {'email_body': email_body, 'to_email': empresa.email,
		        'email_subject': 'Verify your email'}

		print(absurl)
		Util.send_email(data)
		return Response(empresa_data, status=status.HTTP_201_CREATED)

import jwt
from django.conf import settings
class VerificarEmail(APIView):

	def get(self, request):
		token = request.GET.get('token')
		try:
			payload = jwt.decode(token, settings.SECRET_KEY)
			empresa = Empresa.objects.get(id=payload['user_id'])
			if not empresa.is_verified:
				empresa.is_verified = True
				empresa.save()
			return Response({'email': 'Activado correctamente.'}, status=status.HTTP_200_OK)
		except jwt.ExpiredSignatureError as identifier:
			return Response({'error': 'Codigo de activacion expirado'}, status=status.HTTP_400_BAD_REQUEST)
		except jwt.exceptions.DecodeError as identifier:
			return Response({'error': 'Token invalido'}, status=status.HTTP_400_BAD_REQUEST)
