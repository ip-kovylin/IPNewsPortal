from django.urls import path
from .views import AllNews, News, PostCreate, PostUpdate, PostDelete, SearchPost

urlpatterns = [
    path('', AllNews.as_view(), name='all_posts'),
    path('search/', SearchPost.as_view(), name='search_posts'),
    path('<int:id>', News.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete')
]
