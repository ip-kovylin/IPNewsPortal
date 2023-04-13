from django_filters import FilterSet, ModelChoiceFilter, ModelMultipleChoiceFilter
from .models import Post, Category


class PostFilter(FilterSet):
    category = ModelMultipleChoiceFilter(
        field_name='postcategory__through_category',
        queryset=Category.objects.all(),
        label='Category',
        conjoined=True,
    )


    class Meta:
        model = Post
        fields = {
            # поиск по типу поста
            'post_type': ['exact'],
            # поиск по названию
            'headline': ['icontains'],
            'rating': [
                'lt',
                'gt',
            ],
        }
