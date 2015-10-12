# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_auto_20151010_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalBackgroundChoices',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('description', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='medical_background_information',
            field=models.ManyToManyField(to='patients.MedicalBackgroundChoices'),
        ),
    ]
