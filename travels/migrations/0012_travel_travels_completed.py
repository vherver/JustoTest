# Generated by Django 3.0.6 on 2020-05-24 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0011_auto_20200523_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='travels_completed',
            field=models.BigIntegerField(default=0),
        ),
    ]
