# Generated by Django 2.0 on 2019-02-26 05:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_program', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Krai',
        ),
        migrations.AlterField(
            model_name='availabletime',
            name='appointment_date',
            field=models.DateField(default=datetime.datetime(2019, 2, 26, 12, 28, 50, 459442)),
        ),
        migrations.AlterField(
            model_name='availabletime',
            name='appointment_time',
            field=models.TimeField(default=datetime.datetime(2019, 2, 26, 12, 28, 50, 459442)),
        ),
    ]
