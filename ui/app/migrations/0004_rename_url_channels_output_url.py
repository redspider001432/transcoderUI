# Generated by Django 3.2.21 on 2023-11-04 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_channels_udp_stream'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channels',
            old_name='url',
            new_name='output_url',
        ),
    ]
