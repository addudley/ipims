# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patients', '0013_auto_20151011_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosage', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('prescribed_on', models.DateField(default=datetime.date.today, verbose_name='Prescribed on')),
                ('filled_on', models.DateField(blank=True)),
                ('doctor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('medication', models.ForeignKey(to='prescriptions.Medication')),
                ('patient', models.ForeignKey(to='patients.Patient')),
            ],
        ),
    ]
