from django.urls import path
from .views import *

urlpatterns = [
	path('register/', RegisterView.as_view(), name="auth-register"),
	path('email-verify/', VerifyEmail.as_view(), name="auth-email-verify"),
	# path('token/refresh/', TokenRefreshView.as_view(), name='auth-token_refresh'),
]