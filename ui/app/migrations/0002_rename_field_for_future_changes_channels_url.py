# Generated by Django 3.2.21 on 2023-11-03 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channels',
            old_name='field_for_future_changes',
            new_name='url',
        ),
    ]
