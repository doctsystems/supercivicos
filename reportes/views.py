from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ReporteSerializer
from .models import Reporte

from rest_framework_gis.filters import DistanceToPointFilter, DistanceToPointOrderingFilter
from rest_framework_gis.pagination import GeoJsonPagination
from rest_framework.response import Response
from rest_framework import status

class ReporteViewSet(viewsets.ModelViewSet):
	queryset = Reporte.objects.all()
	serializer_class = ReporteSerializer
	distance_filter_field = 'location'
	distance_filter_convert_meters = True
	filter_backends = (DistanceToPointFilter,)
	# filter_backends = (DistanceToPointOrderingFilter, )
	bbox_filter_include_overlapping = True
	pagination_class = GeoJsonPagination

	def create(self, request, *args, **kwargs):
		print('****************')
		print(request.data)
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
