# Generated by Django 2.2.17 on 2021-03-21 15:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0007_auto_20210321_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 23, 15, 44, 44, 136635, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]