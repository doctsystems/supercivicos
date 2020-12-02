from django.urls import path, include
from core.views import Home
# from core.serializers import *


urlpatterns = [
	path('', Home, name="home"),
]

# URLs for Django OAuth Toolkit
# urlpatterns += [
# 	path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
# 	path('users/', UserList.as_view(), name='users'),
# 	path('users/<pk>/', UserDetails.as_view(), name='user-detail'),
# 	path('groups/', GroupList.as_view(), name='groups'),
# ]