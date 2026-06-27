from django.urls import path
from .views import (
    RepositoryListCreateView,
    RepositoryDetailView,
    CodeFileCreateView,
    CodeFileSearchView,
    CriticalFilesView,
)

urlpatterns = [
    path('repositories/', RepositoryListCreateView.as_view(), name='repository-list'),
    path('repositories/<int:pk>/', RepositoryDetailView.as_view(), name='repository-detail'),
    path('files/', CodeFileCreateView.as_view(), name='file-create'),
    path('files/search/', CodeFileSearchView.as_view(), name='file-search'),
    path('files/critical/', CriticalFilesView.as_view(), name='file-critical'),
]