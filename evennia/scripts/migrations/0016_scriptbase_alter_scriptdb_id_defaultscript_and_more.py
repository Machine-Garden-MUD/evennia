# Generated by Django 4.0.2 on 2022-10-31 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scripts", "0015_convert_contrib_paths"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scriptdb",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
