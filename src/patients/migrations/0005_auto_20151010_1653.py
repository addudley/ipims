# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_auto_20151010_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='allergies',
            field=models.ManyToManyField(to='patients.Allergy'),
        ),
    ]
