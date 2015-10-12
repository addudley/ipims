# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_auto_20151010_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='allergies',
            field=models.ManyToManyField(blank=True, to='patients.Allergy'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='medical_background_information',
            field=models.ManyToManyField(blank=True, to='patients.MedicalBackgroundChoice'),
        ),
    ]
