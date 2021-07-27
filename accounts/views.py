from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from .decorator import account_ownership_required
from .forms import AccountUpdateForm
from .models import HelloWorld
# Create your views here.

has_ownership = [
    account_ownership_required,login_required
]

@login_required
def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        return HttpResponseRedirect(reverse('accounts:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accounts/helloworld.html', context={'text':hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:hello_world')
    template_name = 'accounts/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accounts/detail.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accounts:hello_world')
    template_name = 'accounts/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/delete.html'

