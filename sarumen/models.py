from django.db import models
from datetime import datetime
from django.conf import settings


class Category(models.Model):
    name = models.CharField("カテゴリー", max_length=50)
    slug = models.SlugField("英語名", unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField("ハッシュタグ", max_length=255)
    slug = models.SlugField("英語名", unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    thumbnail = models.ImageField(blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    like_num =  models.IntegerField(default=0)

    objects = models.Manager()

    def __str__(self):
        return self.text