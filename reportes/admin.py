from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Reporte, Categoria

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'is_removed')

class ReporteAdmin(LeafletGeoAdmin):
	list_display = ('id', 'categoria', 'descripcion', 'is_removed')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Reporte, ReporteAdmin)