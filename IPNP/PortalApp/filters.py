import django_filters
from django_filters import FilterSet, ModelMultipleChoiceFilter, DateFilter
from .models import Post, Category, Author
from .forms import *


class PostFilter(FilterSet):
    category = ModelMultipleChoiceFilter(
        field_name='postcategory__through_category',
        queryset=Category.objects.all(),
        label='Category',
        conjoined=True,
    )

    author = ModelMultipleChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        label='Author',
    )

    date_time = DateFilter(
        field_name='date_time',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Post later',
        lookup_expr='date__gte'
    )

    class Meta:
        model = Post
        fields = {
            # поиск по типу поста
            'post_type': ['exact'],
            # поиск по названию
            'headline': ['icontains'],
        }
