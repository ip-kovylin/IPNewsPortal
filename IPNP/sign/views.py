from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from django.views.generic.edit import CreateView

from PortalApp.models import Author
from .models import BaseRegisterForm


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'

@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        premium_group.user_set.add(user)
        Author.objects.create(user_id=request.user.pk)
    return redirect('/')

@login_required
def downgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')
    if request.user.groups.filter(name='authors').exists():
        premium_group.user_set.add(user)
    return redirect('/')