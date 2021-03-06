from django.urls import include, path
from rest_framework import routers
from .views import (
    PostViewSet,
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'blog', PostViewSet)



urlpatterns = [
    path('api/', include(router.urls)),
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/comments/new', views.comment_create, name='comment-create'),
    path('post/<int:pk1>/comments/<int:pk2>/edit', views.comment_update, name='comment-update'),
    path('post/<int:pk1>/comments/<int:pk2>/delete', views.comment_delete, name='comment-delete'),
]

