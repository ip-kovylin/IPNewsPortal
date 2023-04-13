from django import template


register = template.Library()


@register.filter()
def censor(value):
    if not isinstance(value,str):
        raise ValueError('Тип должен быть строковый')

    bad_words = ['редиска', 'дурак']

    words = value.split()

    for i in range(len(words)):
        word = words[i]
        if word.lower() in bad_words:
            words[i] =words[i][0] + '*' * len(word)

    censored_value = ' '.join(words)

    return censored_value
