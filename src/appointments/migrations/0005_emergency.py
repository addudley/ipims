# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patients', '0013_auto_20151011_2144'),
        ('appointments', '0004_auto_20151011_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('doctor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('health_condition', models.ForeignKey(to='appointments.HealthCondition')),
                ('patient', models.ForeignKey(to='patients.Patient')),
            ],
        ),
    ]
