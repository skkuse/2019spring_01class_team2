# Generated by Django 2.2.1 on 2019-06-02 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0003_auto_20190602_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
    ]
