# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ivr_call', '0002_auto_20150704_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ivrmodel',
            name='option_type',
            field=models.CharField(default=b'Redirect to', max_length=20, choices=[(b'Redirect to', b'Redirect to'), (b'Add Speak', b'Add Speak')]),
        ),
    ]
