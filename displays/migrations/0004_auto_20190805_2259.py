# Generated by Django 2.2.3 on 2019-08-06 02:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('displays', '0003_auto_20190805_2241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date_time',
        ),
        migrations.AddField(
            model_name='event',
            name='day',
            field=models.DateField(default=datetime.datetime(2019, 8, 6, 2, 59, 0, 630946, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.datetime(2019, 8, 6, 2, 59, 17, 635865, tzinfo=utc)),
            preserve_default=False,
        ),
    ]