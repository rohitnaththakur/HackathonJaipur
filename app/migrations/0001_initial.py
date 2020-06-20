# Generated by Django 3.0.7 on 2020-06-20 04:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetailsOfDoctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=256)),
                ('state', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256, validators=[django.core.validators.EmailValidator('The Entered Email is not valid.')])),
                ('number', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]