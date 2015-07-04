# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ivr_call', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ivrmodel',
            name='option_type',
            field=models.CharField(default=b'RC', max_length=2, choices=[(b'RC', b'Redirect call'), (b'ST', b'Speak this')]),
        ),
        migrations.AddField(
            model_name='ivrmodel',
            name='option_value',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
