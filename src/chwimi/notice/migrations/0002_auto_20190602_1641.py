# Generated by Django 2.2.1 on 2019-06-02 07:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 2, 16, 41, 24, 448516)),
        ),
    ]
