# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('prescriptions', '0002_auto_20151025_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='date',
            field=models.DateField(verbose_name='Date', default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='dosage',
            field=models.PositiveIntegerField(verbose_name='Dosage (mg)'),
        ),
    ]
