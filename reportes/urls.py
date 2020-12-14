from django.urls import path
from .views import ReporteViewSet

reporte_list = ReporteViewSet.as_view({
    'get': 'list'
})
reporte_detail = ReporteViewSet.as_view({
    'get': 'retrieve',
    'post': 'create',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
	path('reportes/', reporte_list, name="reportes-list"),
	path('reporte/<int:pk>', reporte_detail, name="reporte-detail"),
]
