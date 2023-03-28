from django.shortcuts import render
from PortalApp.models import *
from django.contrib.auth.models import User


def index_page(request):
    # Author.objects.create(user=User.objects.get(username='Vlad'))
    # new = Author(user=User.objects.get(pk=4))
    # new.save()
    return render(request, 'index.html')