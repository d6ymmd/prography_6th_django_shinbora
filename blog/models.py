from django.db import models


class Article(models.Model):
    author = models.CharField(max_length=20)
    owner = models.ForeignKey(
        'auth.User', related_name="blog", on_delete=models.CASCADE, null=True
    )
    title = models.CharField(max_length=40)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)