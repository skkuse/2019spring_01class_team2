# Generated by Django 2.2.1 on 2019-06-07 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0016_auto_20190608_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 8, 2, 36, 4, 868785)),
        ),
    ]