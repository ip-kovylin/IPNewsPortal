from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from PortalApp.models import Post, Category
from datetime import datetime
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


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


class SearchPost(ListView):
    model = Post
    ordering = '-date_time'
    template_name = 'search.html'
    context_object_name = 'search_post'    #обращение
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class News(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news_post'        #обращение
    pk_url_kwarg = 'id'


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('PortalApp.add_post')
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('PortalApp.change_post')
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('PortalApp.delete_post')
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('all_posts')


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'upgrade.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_premium'] = not self.request.user.groups.filter(name='premium').exists()
        return context


class CategoriesList(ListView):
    model = Category
    queryset = Category.objects.all()
    ordering = 'category_name'
    template_name = 'categories.html'
    context_object_name = 'categories'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'one_category.html'
    context_object_name = 'one_category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['cat'] = category
        context['subscribers'] = category.subscribers.all()
        return context



@login_required
def upgrade_me(request):
    user = request.user
    author_group = Group.objects.get(name='author')
    if not request.user.groups.filter(name='author').exists():
        author_group.user_set.add(user)
    return redirect('/')


@login_required
def subscribe(request, pk):
    category = Category.objects.get(pk=pk)
    category.subscribers.add(request.user.id)
    return HttpResponseRedirect('http://127.0.0.1:8000/news/categories')


@login_required
def unsubscribe(request, pk):
    category = Category.objects.get(pk=pk)
    category.subscribers.remove(request.user.id)
    return HttpResponseRedirect('http://127.0.0.1:8000/news/categories')
