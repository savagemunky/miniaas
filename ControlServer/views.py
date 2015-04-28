# Python Imports
import os
import subprocess

# Django Imports
from django.contrib.auth.models import User
from ControlServer.models import Hosts, Host_Stats, Containers, Stats_Table, Containers_Table
from django.contrib import auth
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.views import login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
# from models import LoginForm
from django_tables2 import RequestConfig


# Create your views here.
'''
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
'''


# This function defines what information is shown the index / login page
def index_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            HttpResponseRedirect(request, "containers.html")
        else:
            return render(request, '')
    else:
        return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            HttpResponseRedirect(request, "container.html")
        else:
            return render(request, '')
    else:
        return render(request, 'login.html')


# This function defines what information is displayed in the main view
# This function is currently not in use
def main_view(request):
    if request.method == 'POST':
        return render_to_response('main.html')
    else:
        return render(request, 'main.html')


# This function defines what information is displayed on the containers page
def containers_view(request):

    # List containers
    contable = Containers_Table(Host_Stats.objects.all())
    RequestConfig(request).configure(hstable)
    return render(request, 'stats.html', {'statsTable': hstable})

    con_name = "rho"
    con_host_name = "pistack1.local"
    con_ip_address = "172.16.0.101"

    # Create container
    tnet_login = "(sleep 1; echo -e \"pi\r\"; sleep 1; echo -e \"pi\r\"; sleep 2;"
    lxc_create = " echo -e \"sudo lxc-create -n %s -t pi -P /var/lxc/guests\"; sleep 400;" % con_name
    tnet_exit = " echo -e \"exit\r\") | telnet %s" % con_host_name
    con_create_string = "(" + tnet_login + lxc_create + tnet_exit + ")"
    # subprocess.Popen(con_create_string, stdout=subprocess.PIPE)


    # Destroy Container
    lxc_destroy = " echo -e \"sudo lxc-destroy -n %s -f -P /var/lxc/guests\"; sleep 300;" % con_name
    con_destroy_string = "(" + tnet_login + lxc_destroy + tnet_exit + ")"

    # Start Container


    # Stop Container


    return render_to_response(con_create_string)

# This function defines what information is shown on the stats page
def stats_view(request):
    hstable = Stats_Table(Host_Stats.objects.all())
    RequestConfig(request).configure(hstable)
    return render(request, 'stats.html', {'statsTable': hstable})

    #stats_table(request)
    # if request.user.is_authenticated():
        #recentStats = Host_Stats.objects.order_by()
        #return render_to_response()
    # else:
        #return render(request, 'index.html')