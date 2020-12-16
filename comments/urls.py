from django.urls import path
from comments.views import CommentViewSet

comment_list = CommentViewSet.as_view({
    'get': 'list'
})
comment_create = CommentViewSet.as_view({
    'post': 'create'
})
comment_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
	path('comments/list/', comment_list, name="comment-list"),
	path('comments/create/', comment_create, name="comment-create"),
	path('comments/<int:pk>/edit/', comment_detail, name="comment-detail"),
]