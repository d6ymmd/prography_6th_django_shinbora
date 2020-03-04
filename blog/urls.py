from django.urls import path, include
from rest_framework import routers
# from .views import ArticleViewSet

from . import views

app_name = 'blog'

# router = routers.DefaultRouter()
# router.register('Article', ArticleViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', views.ArticleList.as_view(), name='article-list'),
    path('create/', views.ArticleCreate.as_view(), name='article-create'),
    path('<int:pk>/', views.ArticleDetail.as_view(), name='article-detail'),
    path('<int:pk>/update/', views.ArticleUpdate.as_view(), name='article-update'),
    path('<int:pk>/delete/', views.ArticleDelete.as_view(), name='article-delete'),
]