# Generated by Django 3.2 on 2021-05-17 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0009_auto_20210516_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='operation_amount',
            field=models.IntegerField(),
        ),
    ]
