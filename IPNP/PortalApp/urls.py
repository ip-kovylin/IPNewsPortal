from django.urls import path
from .views import AllNews, News, PostCreate, PostUpdate, PostDelete, SearchPost, upgrade_me, CategoriesList, \
    CategoryDetail, subscribe, unsubscribe

urlpatterns = [
    path('', AllNews.as_view(), name='all_posts'),
    path('search/', SearchPost.as_view(), name='search_posts'),
    path('<int:id>', News.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('upgrade/', upgrade_me, name = 'upgrade'),
    path('categories', CategoriesList.as_view(), name='categories_subscribe'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='one_category'),
    path('categories/<int:pk>/subscribe/', subscribe, name='subscribe'),
    path('categories/<int:pk>/unsubscribe/', unsubscribe, name='unsubscribe'),
]
