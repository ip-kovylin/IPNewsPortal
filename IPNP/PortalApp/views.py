from django.shortcuts import render
from PortalApp.models import *
from PortalApp.resources import news, article
from django.db.models import Sum, Avg

def index_page(request):

    Author.update_rating(Author.objects.get(pk=1))

    return render(request, 'index.html')
