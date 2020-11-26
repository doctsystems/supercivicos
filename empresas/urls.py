from django.urls import path
from empresas.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
	path('', ApiHome.as_view(), name="api"),
	path('empresas/', EmpresaAPIView.as_view(), name='empresas'),
	path('direcciones/', DireccionAPIView.as_view(), name='direcciones'),
	path('responsables/', ResponsableAPIView.as_view(), name='responsables'),

	path('registro-empresas/', RegistroEmpresaView.as_view(), name="registro-empresas"),
	path('verificar-email/', VerificarEmail.as_view(), name="verificar-email"),
	path('token-refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]