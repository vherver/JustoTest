# Generated by Django 3.0.6 on 2020-05-24 02:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0007_auto_20200523_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelclients',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
