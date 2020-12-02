from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from allauth.account.views import confirm_email

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include(('core.urls', 'core'), namespace='core')),
	path('api/', include(('empresas.urls', 'empresas'), namespace='empresas')),
]

urlpatterns += [
	url(r'^rest-auth/', include('rest_auth.urls')),
	url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
	url(r'^account/', include('allauth.urls')),
	url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
