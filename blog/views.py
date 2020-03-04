from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer


# class ArticleViewSet(ListAPIView):
#     queryset = Article.objects.all().order_by('-created_at')
#     serializer_class = ArticleSerializer


# class ArticleDetailViewSet(RetrieveAPIView):
#     lookup_field = 'no'
#     queryset = Article.objects.all().order_by('-created_at')
#     serializer_class = ArticleDetailSerializer

