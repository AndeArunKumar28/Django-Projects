# Generated by Django 5.2.4 on 2025-07-08 05:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='images/')),
                ('Description', models.TextField()),
                ('Author', models.CharField(max_length=100)),
                ('Created_on', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
