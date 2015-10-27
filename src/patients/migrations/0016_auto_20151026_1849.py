# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0015_auto_20151026_0312'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='ethnicity',
            field=models.CharField(default='o', choices=[('wh', 'White'), ('bl', 'Black'), ('na', 'Native American'), ('hi', 'Hispanic'), ('as', 'Asian'), ('o', 'Other')], max_length=2),
        ),
        migrations.AddField(
            model_name='patient',
            name='sex',
            field=models.CharField(default='m', choices=[('m', 'Male'), ('f', 'Female')], max_length=1),
        ),
    ]
