from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

from .models import Article
from .serializers import ArticleSerializer


class ArticleList(ListAPIView):
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer


class ArticleDetail(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleUpdate(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDelete(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleCreate(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


