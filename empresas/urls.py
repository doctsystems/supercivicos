from django.urls import path
from empresas.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
	path('', ApiHome.as_view(), name="api"),
	path('empresas/', EmpresaAPIView.as_view(), name='empresas'),
	path('direcciones/', DireccionAPIView.as_view(), name='direcciones'),
	path('responsables/', ResponsableAPIView.as_view(), name='responsables'),

	path('register/', RegisterView.as_view(), name="register"),
	path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]