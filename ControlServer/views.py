# Python Imports
import os
import subprocess

# Django Imports
from django.contrib.auth.models import User
from ControlServer.models import Hosts, Host_Stats, Containers, Stats_Table, Containers_Table, CreateConForm
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
    contable = Containers_Table(Containers.objects.all())
    RequestConfig(request).configure(contable)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        conForm = CreateConForm(request.POST)
        # check whether it's valid:
        if conForm.is_valid():
            # process the data in form.cleaned_data as required
            host_ip = conForm.cleaned_data['host_ip']
            con_name = conForm.cleaned_data['container_name']
            con_ip_address = conForm.cleaned_data['container_ip']
            con_mac_address = conForm.cleaned_data['container_mac']
            con_base_path = "/var/lxc/guests"

            # Setup the telnet command
            tnet_login = "(sleep 1; echo -e \"pi\r\"; sleep 1; echo -e \"pi\r\"; sleep 2;"
            tnet_exit = " echo -e \"exit\r\") | telnet %s" % host_ip

            # Setup Container Config file
            ## Container
            lxcconf01 = " echo -e \"lxc.utsname = %s\"\n > %s/%s.config;" % (con_name, con_base_path, con_name)
            lxcconf02 = " echo -e \"lxc.rootfs = %s/%s/rootfs\"\n >> %s/%s.config" % (con_base_path, con_name, con_base_path, con_name)
            lxcconf03 = " echo -e \"lxc.tty = 4\"\n >> %s/%s.config;" % (con_base_path, con_name)
            lxcconf04 = " echo -e \"lxc.pts = 1024\"\n\n >> %s/%s.config;" % (con_base_path, con_name)

            lxcconf05 = " echo -e \"## Capabilities\"\n >> %s/%s.config;" % (con_base_path, con_name)
            lxcconf06 = " echo -e \"lxc.cap.drop = sys_admin\"\n\n >> %s/%s.config;" % (con_base_path, con_name)

            lxcconf07 = " echo -e \"## Devices\"\n >> %s.config;" % (con_base_path, con_name)
            lxcconf08 = " echo -e \"lxc.cgroup.devices.deny = a\"\n >> %s/%s.config;" % (con_base_path, con_name)
            lxcconf09 = " echo -e \"lxc.cgroup.devices.allow = c 1:3 rwm\"\n >> %s/%s.config;" % (con_base_path, con_name)
            lxcconf10 = " echo -e \"lxc.cgroup.devices.allow = c 1:5 rwm\"\n >> %s/%s.config;" % (con_base_path, con_name)
            lxcconf11 = " echo -e \"lxc.cgroup.devices.allow = c 5:1 rwm\"\n >> %s/%s.config;" % (con_base_path, con_name)
            lxcconf12 = " echo -e \"lxc.cgroup.devices.allow = c 5:0 rwm\"\n >> %s/%s.config;" % (con_base_path, con_name)
            lxcconf13 = " echo -e \"lxc.cgroup.devices.allow = c 4:0 rwm\"\n >> %s/%s.config;" % (con_base_path, con_name)
            lxcconf14 = " echo -e \"lxc.cgroup.devices.allow = c 4:1 rwm\"\n >> %s/%s.config;" % (con_base_path, con_name)
            lxcconf15 = " echo -e \"lxc.cgroup.devices.allow = c 1:9 rwm\"\n >> %s/%s.config;" % (con_base_path, con_name)
            lxcconf16 = " echo -e \"lxc.cgroup.devices.allow = c 1:8 rwm\"\n >> %s/%s.config;" % (con_base_path, con_name)
            lxcconf17 = " echo -e \"lxc.cgroup.devices.allow = c 136:* rwm\"\n >> %s/%s.config;" % (con_base_path, con_name)
            lxcconf18 = " echo -e \"lxc.cgroup.devices.allow = c 5:2 rwm\"\n >> %s/%s.config;" % (con_base_path, con_name)
            lxcconf19 = " echo -e \"lxc.cgroup.devices.allow = c 254:0 rwm\"\n >> %s/%s.config;" % (con_base_path, con_name)

            lxcconf20 = " echo -e \"## Filesystem\"\n >> %s/%s.config;" % (con_base_path, con_name)
            lxcconf21 = " echo -e \"lxc.mount.entry = proc proc proc nodev,noexec,nosuid 0 0\"\n >> %s/%s.config;" % (con_base_path, con_name)
            lxcconf22 = " echo -e \"lxc.mount.entry = sysfs sys sysfs defaults,ro 0 0\"\n\n >> %s/%s.config;" % (con_base_path, con_name)

            lxcconf23 = " echo -e \"## Networking\n\" >> %s/%s.config;" % (con_base_path, con_name)
            lxcconf24 = " echo -e \"lxc.network.type = veth\"\n >> %s/%s.config;" % (con_base_path, con_name)
            lxcconf25 = " echo -e \"lxc.network.flags = up\"\n >> %s/%s.config;" % (con_base_path, con_name)
            lxcconf26 = " echo -e \"lxc.network.link = br0\"\n >> %s/%s.config;" % (con_base_path, con_name)
            lxcconf27 = " echo -e \"#lxc.network.name = eth0\"\n >> %s/%s.config;" % (con_base_path, con_name)
            lxcconf28 = " echo -e \"lxc.network.hwaddr = %s\"\n >> %s/%s.config;" % (con_mac_address, con_base_path, con_name)
            lxcconf29 = " echo -e \"lxc.network.ipv4 = %s/24\"\n >> %s/%s.config;" % (con_ip_address, con_base_path, con_name)
            lxcconf30 = " echo -e \"lxc.network.ipv4.gateway = 172.16.0.254\"\n >> %s/%s.config;" % (con_base_path, con_name)

            conConfig = (lxcconf01 + lxcconf02 + lxcconf03 + lxcconf04 + lxcconf05 + lxcconf06 + lxcconf07 + lxcconf08 +
                         lxcconf09 + lxcconf10 + lxcconf11 + lxcconf12 + lxcconf13 + lxcconf14 + lxcconf15 + lxcconf16 +
                         lxcconf17 + lxcconf18 + lxcconf19 + lxcconf20 + lxcconf21 + lxcconf22 + lxcconf23 + lxcconf24 +
                         lxcconf25 + lxcconf26 + lxcconf27 + lxcconf28 + lxcconf29 + lxcconf30)

            # Create container
            lxc_create = " echo -e \"sudo lxc-create -n %s -t pi -f %s/%s.config -P %s\"; sleep 400;" % (
                con_name, con_base_path, con_name, con_base_path)
            con_create_string = tnet_login + conConfig + lxc_create + tnet_exit

            try:
                subprocess.Popen(con_create_string, stdout=subprocess.PIPE)
                conForm.save()
            except Exception as e:
                print '%s, (%s)' % (e.message, type(e))

            # Redirect to a new URL:
            return HttpResponseRedirect('/containers/')

    # if a GET (or any other method) we'll create a blank form
    else:
        conForm = CreateConForm()
        # return render(request, 'containers.html', {'cform': conForm})





    # Destroy Container
    # lxc_destroy = " echo -e \"sudo lxc-destroy -n %s -f -P /var/lxc/guests\"; sleep 300;" % con_name
    # con_destroy_string = "(" + tnet_login + lxc_destroy + tnet_exit + ")"
    # conDestroy = Containers.objects.get(container_name=con_name)
    # conDestroy.delete()

    # Start Container
    #lxc_start = " echo -e \"sudo lxc-start -n %s -P /var/lxc/guests\"; sleep 300;" % con_name
    #con_start_string = "(" + tnet_login + lxc_start + tnet_exit + ")"

    # Stop Container
    #lxc_stop = " echo -e \"sudo lxc-stop -n %s -P /var/lxc/guests\"; sleep 300;" % con_name
    #con_stop_string = "(" + tnet_login + lxc_stop + tnet_exit + ")"

    return render(request, 'containers.html', {'conTable': contable, 'cform': conForm})


# This function defines what information is shown on the stats page
def stats_view(request):
    hstable = Stats_Table(Host_Stats.objects.all())
    RequestConfig(request).configure(hstable)
    return render(request, 'stats.html', {'statsTable': hstable})

    # stats_table(request)
    # if request.user.is_authenticated():
    #recentStats = Host_Stats.objects.order_by()
    #return render_to_response()
    # else:
    #return render(request, 'index.html')