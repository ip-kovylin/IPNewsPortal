import datetime

from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed, pre_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from .models import PostCategory, Post, Author
from IPNP import settings


def send_notifications(preview, pk, headline, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=headline,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    print(settings.DEFAULT_FROM_EMAIL)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers_emails = []

        for cat in categories:
            subscribers = cat.subscribers.all()
            subscribers_emails += [s.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk, instance.headline, subscribers_emails)


@receiver(pre_save, sender=Post)
def check_for_saves(sender, instance, **kwargs):
    current_author = instance.author_id
    last_day = date_time=datetime.datetime.now()-datetime.timedelta(hours=24)
    posts = Post.objects.filter(author=Author.objects.get(id=current_author), date_time__gte=last_day)
    if len(posts) > 2:
        raise Exception("Извините, вы не можете публиковать более 3 постов в день.")
 