# Generated by Django 3.2 on 2021-05-05 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eng', '0002_alter_safety_opertion_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Safety',
        ),
        migrations.DeleteModel(
            name='Site',
        ),
    ]
