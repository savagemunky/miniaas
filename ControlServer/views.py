# from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def hello(request):
    return HttpResponse("Hello World")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><head>The Time</head><body><p>The current time is %s.</p></body</html>" % now
    return HttpResponse(html)


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/time/")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })