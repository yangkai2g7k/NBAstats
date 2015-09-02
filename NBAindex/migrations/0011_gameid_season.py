# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NBAindex', '0010_teamprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameid',
            name='season',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]
