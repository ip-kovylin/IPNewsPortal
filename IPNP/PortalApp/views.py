from django.shortcuts import render
# from PortalApp.models import *
# from PortalApp.resources import news, article
# from django.db.models import Sum, Avg, Max

def index_page(request):
    return render(request, 'index.html')
