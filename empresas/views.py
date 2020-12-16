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

			'Empresas List':'/api/empresas/list',
			'Empresas Create':'/api/empresas/create',
			'Empresas Detail-Update':'/api/empresas/<int:pk>/edit/',

			'Verificacion de email':'/api/verificar-email/',

			'Reportes List':'/api/reportes/list',
			'Reportes Create':'/api/reportes/create',
			'Reportes Detail-Update':'/api/reportes/<int:pk>/edit/',

			'Comments List':'/api/comments/list',
			'Comments Create':'/api/comments/create',
			'Comments Detail-Update':'/api/comments/<int:pk>/edit/',

			'Rates List':'/api/rates/list',
			'Rates Create':'/api/rates/create',
			'Rates Detail-Update':'/api/rates/<int:pk>/edit/',

			'Stickers List':'/api/stickers/list',
			'Stickers Create':'/api/stickers/create',
			'Stickers Detail-Update':'/api/stickers/<int:pk>/edit/',
                        
                        'Send the authentication PIN to an email': '/authentication/getpin',
                        'Get the access token with the PIN': '/authentication/token',
		}
		return Response(api_urls)

from rest_framework import viewsets
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
class EmpresaViewSet(viewsets.ModelViewSet):
	queryset = Empresa.objects.filter(is_verified=True)
	serializer_class = EmpresaSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data)
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

