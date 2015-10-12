# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_healthcondition_doctors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='health_condition', chained_model_field='get_full_name()', to=settings.AUTH_USER_MODEL),
        ),
    ]
