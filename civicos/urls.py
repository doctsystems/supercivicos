from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include(('core.urls', 'core'), namespace='core')),
	path('api/', include(('empresas.urls', 'empresas'), namespace='empresas')),
	# path('auth/', include(('authentication.urls', 'auth'), namespace='auth')),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
