# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0014_patient_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='profile_picture',
            field=models.ImageField(upload_to='images/', null=True, blank=True),
        ),
    ]
