from django.urls import path
from rate.views import RateViewSet

rate_list = RateViewSet.as_view({
    'get': 'list'
})
rate_create = RateViewSet.as_view({
    'post': 'create'
})
rate_detail = RateViewSet.as_view({
    'get': 'retrieve',
    'put': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
	path('rates/list/', rate_list, name="rate-list"),
	path('rates/create/', rate_create, name="rate-create"),
	path('rates/<int:pk>/edit/', rate_detail, name="rate-detail"),
]