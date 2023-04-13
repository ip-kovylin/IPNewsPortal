from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    headline = forms.CharField(min_length=10)

    class Meta:
        model = Post
        fields = [
            'author',
            'post_type',
            'category',
            'headline',
            'text',
            'rating',
        ]

    def clean(self):
        cleaned_data = super().clean()
        headline = cleaned_data.get('headline')
        text = cleaned_data.get('text')
        if text == headline or len(text) < 20:
            raise ValidationError({
                'text': 'Текст не может быть одинаковым с заголовком и быть менее 20 символов'
            })

        return cleaned_data
