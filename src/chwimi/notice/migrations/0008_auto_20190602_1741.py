# Generated by Django 2.2.1 on 2019-06-02 08:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0007_auto_20190602_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 2, 17, 41, 40, 727164)),
        ),
    ]
