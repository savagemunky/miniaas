import os
import subprocess
from django.contrib.auth.models import User
from ControlServer.models import Hosts
from ControlServer.models import Host_Stats
from ControlServer.models import Containers
from django.contrib import auth
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.views import login
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
# from models import LoginForm


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

# This function defines what information is displayed in the main view
# This function is currently not in use
def main_view(request):
    if request.method == 'POST':
        return render_to_response('main.html')
    else:
        return render(request, 'main.html')

# This function defines what information is displayed on the containers page
def containers_view(request):
    con_name = "rho"
    con_ip = "0.0.0.0"  # This will be set later - the containers use DHCP
    con_host_ip = "172.16.0.1"

    # If the user is authenticated
    if request.user.is_authenticated():
        # Create container
        subprocess.Popen("(sleep 1; echo -e \"pi\r\"; sleep 1; echo -e \"pi\r\"; sleep 2; echo -e \"sudo lxc-create -n rho -t pi -P /var/lxc/guests\"; sleep 400; echo -e \"exit\r\") | telnet 172.16.0.1")
    # Otherwise return the user to the index screen
    else:
        return render(request, 'index.html')

# This function defines what information is shown on the stats page
def stats_view(request):
    # if request.user.is_authenticated():
        recentStats = Host_Stats.objects.order_by()
        return render_to_response()
    # else:
        #return render(request, 'index.html')