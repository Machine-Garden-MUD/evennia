# Generated by Django 3.2.3 on 2021-05-20 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0003_auto_20190128_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helpentry',
            name='db_staff_only',
        ),
        migrations.AddField(
            model_name='helpentry',
            name='db_date_created',
            field=models.DateTimeField(auto_now=True, verbose_name='creation date'),
        ),
    ]