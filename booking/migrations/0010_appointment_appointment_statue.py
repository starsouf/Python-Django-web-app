# Generated by Django 3.1.2 on 2021-09-20 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_auto_20210920_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointment_statue',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
