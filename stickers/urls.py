from django.urls import path
from stickers.views import StickersViewSet

sticker_list = StickersViewSet.as_view({
    'get': 'list'
})
sticker_create = StickersViewSet.as_view({
    'post': 'create'
})
sticker_detail = StickersViewSet.as_view({
    'get': 'retrieve',
    'put': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
	path('stickers/list/', sticker_list, name="sticker-list"),
	path('stickers/create/', sticker_create, name="sticker-create"),
	path('stickers/<int:pk>/edit/', sticker_detail, name="sticker-detail"),
]