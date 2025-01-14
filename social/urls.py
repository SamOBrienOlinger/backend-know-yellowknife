from django.urls import path
from .views import PostListCreateView, PostDetailView, CommentListCreateView, LikeListCreateView, FollowerListCreateView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('likes/', LikeListCreateView.as_view(), name='like-list-create'),
    path('followers/', FollowerListCreateView.as_view(), name='follower-list-create'),
]
