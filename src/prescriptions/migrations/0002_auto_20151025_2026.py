# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prescriptions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescription',
            old_name='prescribed_on',
            new_name='date',
        ),
    ]
