from django.urls import path

from posts.views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('view/<int:pk>/', PostDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
]