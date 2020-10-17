from django.urls import path
from empresas.views import EmpresaAPIView, DireccionAPIView, ResponsableAPIView

urlpatterns = [
	path('', EmpresaAPIView.as_view(), name='home'),
	path('direcciones/', DireccionAPIView.as_view(), name='dirs'),
	path('responsables/', ResponsableAPIView.as_view(), name='resp'),
]