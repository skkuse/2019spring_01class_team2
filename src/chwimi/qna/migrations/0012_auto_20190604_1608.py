# Generated by Django 2.2.1 on 2019-06-04 07:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0011_auto_20190604_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 4, 16, 8, 20, 501819)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 4, 16, 8, 20, 501819)),
        ),
    ]
