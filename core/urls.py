from django.urls import path
from core.views import Home

urlpatterns = [
	path('', Home, name="home"),
]