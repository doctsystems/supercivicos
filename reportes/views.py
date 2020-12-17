from django.shortcuts import render
from rest_framework import viewsets
from reportes.serializers import ReporteSerializer, CategoriaSerializer
from reportes.models import Reporte, Categoria

from rest_framework_gis.filters import DistanceToPointFilter, DistanceToPointOrderingFilter
from rest_framework_gis.pagination import GeoJsonPagination
from rest_framework.response import Response
from rest_framework import status

class CategoriaViewSet(viewsets.ModelViewSet):
	queryset = Categoria.objects.filter(is_removed=False)
	serializer_class = CategoriaSerializer

	def perform_destroy(self, instance):
		instance.is_removed = True
		instance.save()
		# instance.delete()

class ReporteViewSet(viewsets.ModelViewSet):
	queryset = Reporte.objects.filter(is_removed=False)
	serializer_class = ReporteSerializer
	distance_filter_field = 'location'
	distance_filter_convert_meters = True
	filter_backends = (DistanceToPointFilter,)
	# filter_backends = (DistanceToPointOrderingFilter, )
	bbox_filter_include_overlapping = True
	pagination_class = GeoJsonPagination

	def perform_destroy(self, instance):
		instance.is_removed = True
		instance.save()
