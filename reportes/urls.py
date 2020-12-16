from django.urls import path
from reportes.views import ReporteViewSet

reporte_list = ReporteViewSet.as_view({
    'get': 'list'
})
reporte_create = ReporteViewSet.as_view({
    'post': 'create'
})
reporte_detail = ReporteViewSet.as_view({
    'get': 'retrieve',
    'put': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('reportes/list/', reporte_list, name="reporte-list"),
    path('reportes/create/', reporte_create, name="reporte-create"),
    path('reportes/<int:pk>/edit/', reporte_detail, name="reporte-detail"),
]
