from django.db import models
from django.contrib.auth.models import User
from PortalApp.resources import PostType, news
from django.db.models import Sum


class Author(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, unique=True)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        post_rating = self.post_set.aggregate(postRating=Sum('rating'))
        sum_post_rating = 0
        sum_post_rating = post_rating.get('postRating')

        comment_rating = self.user.comment_set.aggregate(commentRating=Sum('rating'))
        sum_comment_rating = 0
        sum_comment_rating = comment_rating.get('commentRating')

        self.rating = sum_post_rating * 3 + sum_comment_rating
        self.save()

    def __str__(self):
        return f'User: {self.user}, rating: {self.rating}'


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'category_name: {self.category_name}'


class Post(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    post_type = models.CharField(max_length=4, choices=PostType, default=news)
    date_time = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category', through='PostCategory')
    headline = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[:124]}...'

    def __str__(self):
        return f'''author: {self.author}, post_type: {self.post_type}', date_time: {self.date_time}'
        , category: {self.category}', headline: {self.headline}', text: {self.text}'
        , rating: {self.rating}'''


class PostCategory(models.Model):
    through_post = models.ForeignKey('Post', on_delete=models.CASCADE)
    through_category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    date_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
