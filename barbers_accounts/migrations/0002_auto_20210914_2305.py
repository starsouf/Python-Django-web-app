# Generated by Django 3.1.2 on 2021-09-15 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbers_accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barber',
            name='barber_age',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='barber',
            name='barber_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='barber',
            name='barber_phone',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='barber',
            name='barber_pic',
            field=models.ImageField(blank=True, default='', upload_to='media/'),
        ),
    ]
