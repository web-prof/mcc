# Generated by Django 3.2 on 2021-05-13 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0007_auto_20210513_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='operation_approval',
            field=models.BooleanField(default=False),
        ),
    ]
