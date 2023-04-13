from django.urls import path
from .views import AllNews, News, create_post

urlpatterns = [
    path('', AllNews.as_view()),
    path('<int:id>', News.as_view()),
    path('create/', create_post, name='create_post'),
]
