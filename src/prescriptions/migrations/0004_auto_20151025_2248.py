# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prescriptions', '0003_auto_20151025_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='filled_on',
            field=models.DateField(null=True, blank=True),
        ),
    ]
