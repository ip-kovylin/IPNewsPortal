from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from PortalApp.models import Post
from datetime import datetime
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy


def index_page(request):
    return render(request, 'index.html')


class AllNews(ListView):
    model = Post
    ordering = '-date_time'
    template_name = 'allnews.html'
    context_object_name = 'all_news'    #обращение
    paginate_by = 10


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['breaking_news'] = None
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class News(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news_post'        #обращение
    pk_url_kwarg = 'id'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('all_posts')
