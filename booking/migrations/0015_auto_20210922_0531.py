# Generated by Django 3.1.2 on 2021-09-22 09:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_auto_20210921_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='when',
            field=models.DateField(default=datetime.date(2021, 9, 22)),
        ),
    ]
