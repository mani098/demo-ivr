# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ivr_call', '0003_auto_20150704_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ivrmodel',
            name='option_value',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
