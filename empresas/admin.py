from django.contrib import admin
from empresas.models import Direccion, Empresa, Responsable

class EmpresaAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'email', 'telefono') 
	# search_fields = ('nombre',)

class DireccionAdmin(admin.ModelAdmin):
	list_display = ('id', 'calle', 'colonia', 'ciudad', 'pais') 
	# search_fields = ('nombre',)

class ResponsableAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombres', 'apellidos', 'telefono') 
	# search_fields = ('nombre',)

admin.site.register(Direccion, DireccionAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Responsable, ResponsableAdmin)