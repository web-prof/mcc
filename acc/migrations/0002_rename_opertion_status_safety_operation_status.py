# Generated by Django 3.2 on 2021-05-05 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='safety',
            old_name='opertion_status',
            new_name='operation_status',
        ),
    ]
