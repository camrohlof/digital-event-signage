# Generated by Django 2.2.3 on 2019-09-14 06:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('displays', '0005_auto_20190901_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='test',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 14, 2, 23, 12, 876382)),
            preserve_default=False,
        ),
    ]
