# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Containers',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('container_ip', models.CharField(max_length=15)),
                ('container_mac', models.CharField(max_length=17)),
                ('container_name', models.CharField(max_length=50)),
                ('container_cpu_limit', models.IntegerField(max_length=3)),
                ('container_ram_limit', models.IntegerField(max_length=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Host_Stats',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('log_time', models.DateTimeField(auto_now_add=True)),
                ('cpu_use', models.IntegerField(max_length=3)),
                ('mem_total', models.IntegerField(max_length=6)),
                ('mem_used', models.IntegerField(max_length=6)),
                ('mem_free', models.IntegerField(max_length=6)),
                ('store_total', models.IntegerField(max_length=7)),
                ('store_used', models.IntegerField(max_length=7)),
                ('store_free', models.IntegerField(max_length=7)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('ip_address', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('mac_address', models.CharField(max_length=17)),
                ('host_name', models.CharField(max_length=50)),
                ('online', models.BooleanField(default=False)),
                ('reserved', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='host_stats',
            name='ip_address',
            field=models.ForeignKey(to='ControlServer.Hosts'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='containers',
            name='host_ip',
            field=models.ForeignKey(to='ControlServer.Hosts'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='containers',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
