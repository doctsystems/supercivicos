from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Reporte, Categoria

class ReporteAdmin(LeafletGeoAdmin):
	list_display = ('id', 'categoria', 'descripcion')

admin.site.register(Reporte, ReporteAdmin)
admin.site.register(Categoria)