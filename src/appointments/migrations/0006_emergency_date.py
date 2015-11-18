# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_emergency'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergency',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 18, 1, 44, 20, 732754, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
