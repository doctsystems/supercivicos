from django.urls import path
from empresas.views import HelloAPIView, EmpresaAPIView

urlpatterns = [
	path('', EmpresaAPIView.as_view(), name='home'),
	path('hello/', HelloAPIView.as_view(), name='hello'),
]