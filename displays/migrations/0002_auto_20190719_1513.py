# Generated by Django 2.2.3 on 2019-07-19 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('displays', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_type',
            new_name='eventType',
        ),
        migrations.RemoveField(
            model_name='event',
            name='date_added',
        ),
    ]