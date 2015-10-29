# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0017_auto_20151026_1850'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LabReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('request_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('status', models.CharField(choices=[('r', 'Requested'), ('ip', 'In Progress'), ('c', 'Complete')], max_length=2)),
                ('doctor_notes', models.TextField(null=True, blank=True)),
                ('results', models.TextField(null=True, blank=True)),
                ('update_date', models.DateField(null=True, verbose_name='Date', blank=True)),
                ('doctor', models.ForeignKey(related_name='doctor', to=settings.AUTH_USER_MODEL)),
                ('lab_technician', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='lab_technician', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='labreport',
            name='lab_test',
            field=models.ForeignKey(to='labreports.LabTest'),
        ),
        migrations.AddField(
            model_name='labreport',
            name='patient',
            field=models.ForeignKey(to='patients.Patient'),
        ),
    ]
