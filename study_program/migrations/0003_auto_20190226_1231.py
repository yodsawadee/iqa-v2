# Generated by Django 2.0 on 2019-02-26 05:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_program', '0002_auto_20190226_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabletime',
            name='appointment_date',
            field=models.DateField(default=datetime.datetime(2019, 2, 26, 12, 31, 17, 462468)),
        ),
        migrations.AlterField(
            model_name='availabletime',
            name='appointment_time',
            field=models.TimeField(default=datetime.datetime(2019, 2, 26, 12, 31, 17, 462468)),
        ),
    ]