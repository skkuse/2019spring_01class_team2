# Generated by Django 2.2.1 on 2019-05-26 06:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 26, 15, 38, 42, 717072)),
        ),
    ]