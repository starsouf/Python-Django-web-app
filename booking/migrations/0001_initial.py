# Generated by Django 3.1.2 on 2021-08-31 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='barber_gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hairCuts', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('client_phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='barber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barber_name', models.CharField(max_length=100)),
                ('barber_age', models.CharField(max_length=2)),
                ('barber_phone', models.CharField(max_length=100)),
                ('barber_email', models.EmailField(max_length=254)),
                ('barber_pic', models.ImageField(upload_to='')),
                ('barber_hairCuts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.barber_gallery')),
            ],
        ),
    ]
