# Generated by Django 2.2.3 on 2019-09-14 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('displays', '0006_event_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='test',
            new_name='dayTime',
        ),
        migrations.RemoveField(
            model_name='event',
            name='day',
        ),
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
    ]