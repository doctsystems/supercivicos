from django.urls import path
from reportes.views import ReporteViewSet, CategoriaViewSet

reporte_list = ReporteViewSet.as_view({'get': 'list'})
reporte_create = ReporteViewSet.as_view({'post': 'create'})
reporte_detail = ReporteViewSet.as_view({'get': 'retrieve','put': 'partial_update','delete': 'destroy'})

urlpatterns = [
	path('reportes/list/', reporte_list, name="reporte-list"),
	path('reportes/create/', reporte_create, name="reporte-create"),
	path('reportes/<int:pk>/edit/', reporte_detail, name="reporte-detail"),
]

categoria_list = CategoriaViewSet.as_view({'get': 'list'})
categoria_create = CategoriaViewSet.as_view({'post': 'create'})
categoria_detail = CategoriaViewSet.as_view({'get': 'retrieve',	'put': 'partial_update', 'delete': 'destroy'})

urlpatterns += [
	path('categorias/list/', categoria_list, name="categoria-list"),
	path('categorias/create/', categoria_create, name="categoria-create"),
	path('categorias/<int:pk>/edit/', categoria_detail, name="categoria-detail"),
]
