# Generated by Django 2.2.1 on 2019-06-04 06:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0010_auto_20190602_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 4, 15, 55, 25, 863736)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 4, 15, 55, 25, 862749)),
        ),
    ]