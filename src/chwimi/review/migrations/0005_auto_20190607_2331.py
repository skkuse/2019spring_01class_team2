# Generated by Django 2.2.1 on 2019-06-07 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_auto_20190605_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 7, 23, 31, 20, 708379)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 7, 23, 31, 20, 707380)),
        ),
    ]
