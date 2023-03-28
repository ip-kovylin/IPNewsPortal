from django.db import models
from django.contrib.auth.models import User
from PortalApp.resources import PostType, news


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=4, choices=PostType, default=news)
    date_time = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    headline = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    date_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
