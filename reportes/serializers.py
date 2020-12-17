from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from reportes.models import Categoria, Reporte
from videos.models import Video
from videos.serializers import VideoSerializer
from drf_base64.fields import Base64FileField

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Categoria
		fields = ['id', 'nombre']
		
class ReporteSerializer(GeoFeatureModelSerializer):
	categoria = CategoriaSerializer(read_only=True)
	categoriaId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Categoria.objects.all(), source='categoria')
	# video2 = Base64FileField(required=False)

	class Meta:
		model = Reporte
		geo_field = 'location'
		auto_bbox = True
		fields = ['id', 'usuario', 'categoria', 'categoriaId', 'video', 'descripcion', 'location']
