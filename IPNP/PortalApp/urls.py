from django.urls import path
from .views import AllNews, News

urlpatterns = [
    path('', AllNews.as_view()),
    path('<int:id>', News.as_view()),
]
