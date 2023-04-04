from django.shortcuts import render
from django.views.generic import ListView, DetailView
from PortalApp.models import Post
# from PortalApp.resources import news, article
# from django.db.models import Sum, Avg, Max

def index_page(request):
    return render(request, 'index.html')


class AllNews(ListView):
    model = Post
    ordering = 'date_time'
    template_name = 'allnews.html'
    context_object_name = 'all_news'


class News(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    pk_url_kwarg = 'id'