from django.urls import path, include
from rest_framework import routers
from .views import ArticleViewSet

from . import views

app_name = 'blog'

router = routers.DefaultRouter()
router.register('Article', ArticleViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]