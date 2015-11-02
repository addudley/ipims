# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_emergency'),
        ('patients', '0017_auto_20151026_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField()),
                ('notes', models.TextField(null=True, blank=True)),
                ('resolved', models.BooleanField(default=False)),
                ('health_condition', models.ForeignKey(to='appointments.HealthCondition')),
                ('patient', models.ForeignKey(to='patients.Patient')),
            ],
        ),
    ]
