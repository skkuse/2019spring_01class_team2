# Generated by Django 2.2.1 on 2019-06-07 16:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0015_auto_20190607_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 8, 1, 1, 28, 364033)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 8, 1, 1, 28, 363036)),
        ),
    ]