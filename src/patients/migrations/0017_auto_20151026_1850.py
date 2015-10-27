# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0016_auto_20151026_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='ethnicity',
            field=models.CharField(choices=[('wh', 'White'), ('bl', 'Black'), ('na', 'Native American'), ('hi', 'Hispanic'), ('as', 'Asian'), ('o', 'Other')], max_length=2),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1),
        ),
    ]
