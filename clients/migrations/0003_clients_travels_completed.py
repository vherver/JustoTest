# Generated by Django 3.0.6 on 2020-05-24 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20200523_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='travels_completed',
            field=models.BigIntegerField(default=0),
        ),
    ]
