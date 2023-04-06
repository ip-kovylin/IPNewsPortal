from django.shortcuts import render
from django.views.generic import ListView, DetailView
from PortalApp.models import Post
from datetime import datetime


def index_page(request):
    return render(request, 'index.html')


class AllNews(ListView):
    model = Post
    ordering = '-date_time'
    template_name = 'allnews.html'
    context_object_name = 'all_news'    #обращение

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['breaking_news'] = None
        return context


class News(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news_post'        #обращение
    pk_url_kwarg = 'id'