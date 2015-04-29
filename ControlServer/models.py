# Import classes
from django.db import models
from django.contrib.auth.models import User
import django_tables2 as tables

# The models.py is where all classes that deal with or handle
# data live. This primarily means databases tables and attributes
# but could also include various forms of data manipulation,
# extrapolation, or analytics.
# Most of these classes are fairly straight-forward as they relate
# directly to the database tables for the project.

# Note: The auth_user database table is automatically generated
# by Django as part of the Django admin interface


# Hosts Class
# This class is used to create the Database table for Host information
class Hosts(models.Model):
    ip_address = models.CharField(primary_key=True, max_length=15)
    mac_address = models.CharField(max_length=17)
    host_name = models.CharField(max_length=50)
    online = models.BooleanField(default=False)
    reserved = models.NullBooleanField(default=False, null=True)


# Host_Stats Class
# This class is used to create the Database table for Host Statistics
class Host_Stats(models.Model):
    id = models.AutoField(primary_key=True)
    log_time = models.DateTimeField(auto_now_add=True)
    ip_address = models.ForeignKey('Hosts')
    cpu_use = models.IntegerField(max_length=3,)
    mem_total = models.IntegerField(max_length=6)
    mem_used = models.IntegerField(max_length=6)
    mem_free = models.IntegerField(max_length=6)
    store_total = models.IntegerField(max_length=7)
    store_used = models.IntegerField(max_length=7)
    store_free = models.IntegerField(max_length=7)


# Container Class
# This class is used to create the Database table for Container information
class Containers (models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User)
    host_ip = models.ForeignKey('Hosts')
    container_ip = models.CharField(max_length=15)
    container_mac = models.CharField(max_length=17)
    container_name = models.CharField(max_length=50)
    container_cpu_limit = models.IntegerField(max_length=3)
    container_ram_limit = models.IntegerField(max_length=6)


# Table class for Containers
# This class is used to create a table from the Containers model
class Containers_Table(tables.Table):
    host_ip_address = tables.Column(accessor='host_ip.ip_address')
    host_name = tables.Column(accessor='host_ip.host_name')

    class Meta:
        model = Containers
        attrs = {"class": "table table-striped"}
        fields = ("container_name", "container_ip")
        sequence = ("host_name", "host_ip_address", "container_name", "container_ip")


# Table class for Host Stats
# This class is used to create tables from the Host_Stats model
class Stats_Table(tables.Table):
    ip_address = tables.Column(accessor='ip_address.ip_address')
    host_name = tables.Column(accessor='ip_address.host_name')
    log_time = tables.DateTimeColumn(format='Y/m/d H:i:s')

    class Meta:
        model = Host_Stats
        attrs = {"class": "table table-striped"}
        fields = ("log_time", "cpu_use", "mem_used", "mem_free", "store_total", "store_free")
        sequence = ("log_time", "host_name", "ip_address", "cpu_use", "mem_used", "mem_free", "store_total", "store_free")

