from celery import shared_task
import datetime, time
from django.conf import settings

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from PortalApp.models import Post, Category, CategorySubscriber


@shared_task            #test task
def hello():
    time.sleep(10)
    print('Hello from tasks')


@shared_task            #test task
def printer(x):
    for i in range(x):
        time.sleep(1)
        print(i + 1)


@shared_task
def send_email_task(pk):
    post = Post.objects.get(pk=pk)
    categories = post.category.all()
    title = post.headline
    subscribers_emails = []
    for category in categories:
        subscribers_users = category.subscribers.all()
        for sub_user in subscribers_users:
            subscribers_emails.append(sub_user.email)
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': post.preview,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_emails,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def weekly_notifications_task():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(date_time__gte=last_week)
    categories = set(posts.values_list('category__category_name', flat=True))
    subscribers = set(Category.objects.filter(category_name__in=categories).values_list('subscribers__email', flat=True))
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, "text/html")

    msg.send()
