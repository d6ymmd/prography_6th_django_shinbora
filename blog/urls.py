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
    path('<int:pk>/', views.ArticleDetail.as_view(), name='article-detail'),
    # path('users/', views.UserList.as_view(), name='user-list'),
    # path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]