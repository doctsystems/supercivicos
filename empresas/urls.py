from django.urls import path
from empresas.views import *

urlpatterns = [
	path('', apiOverview.as_view(), name="api"),
	path('list/', EmpresaList, name='list'),
	path('create/', EmpresaCreate, name='create'),
	path('empresas/', EmpresaAPIView.as_view(), name='empresas'),
	path('direcciones/', DireccionAPIView.as_view(), name='direcciones'),
	path('responsables/', ResponsableAPIView.as_view(), name='responsables'),
]