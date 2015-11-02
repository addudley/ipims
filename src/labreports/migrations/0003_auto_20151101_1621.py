# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('labreports', '0002_auto_20151028_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labreport',
            name='request_date',
            field=models.DateField(verbose_name='Lab Request Date', default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='labreport',
            name='update_date',
            field=models.DateField(null=True, verbose_name='Last updated', blank=True),
        ),
    ]
