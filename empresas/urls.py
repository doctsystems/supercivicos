from django.urls import path
from empresas.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

empresa_list = EmpresaViewSet.as_view({
    'get': 'list'
})
empresa_create = EmpresaViewSet.as_view({
    'post': 'create'
})
empresa_detail = EmpresaViewSet.as_view({
    'get': 'retrieve',
    'put': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
	path('', ApiHome.as_view(), name="api"),
	path('empresas/list/', empresa_list, name="reporte-list"),
	path('empresas/create/', empresa_create, name="reporte-create"),
	path('empresas/<int:pk>/edit/', empresa_detail, name="reporte-detail"),
	path('verificar-email/', VerificarEmail.as_view(), name="verificar-email"),
	path('token-refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]