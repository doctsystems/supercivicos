from django.shortcuts import render
from rest_framework import viewsets
from reportes.serializers import ReporteSerializer, CategoriaSerializer
from reportes.models import Reporte, Categoria

from rest_framework_gis.filters import DistanceToPointFilter, DistanceToPointOrderingFilter
from rest_framework_gis.pagination import GeoJsonPagination
from rest_framework.response import Response
from rest_framework import status

class CategoriaViewSet(viewsets.ModelViewSet):
	queryset = Categoria.objects.filter(is_active=True)
	serializer_class = CategoriaSerializer

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object()
		self.perform_destroy(instance)
		return Response(status=status.HTTP_204_NO_CONTENT)

class ReporteViewSet(viewsets.ModelViewSet):
	queryset = Reporte.objects.filter(is_active=True)
	serializer_class = ReporteSerializer
	distance_filter_field = 'location'
	distance_filter_convert_meters = True
	filter_backends = (DistanceToPointFilter,)
	# filter_backends = (DistanceToPointOrderingFilter, )
	bbox_filter_include_overlapping = True
	pagination_class = GeoJsonPagination

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
