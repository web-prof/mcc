# Generated by Django 3.2 on 2021-05-12 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0004_auto_20210506_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='operations_document',
            field=models.ImageField(blank=True, null=True, upload_to='operation_documents/'),
        ),
    ]
