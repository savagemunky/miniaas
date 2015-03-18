from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from models import LoginForm


# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/index/")
    else:
        form = UserCreationForm()
    return render(request, "/register/", {
        'form': form,
    })


def index_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            return render(request, '')
    else:
        return render(request, 'index.html')


def main_view(request):
    if request.method == 'POST':
        return render_to_response('main.html')
    else:
        return render(request, 'main.html')

