# Generated by Django 4.2.9 on 2024-01-23 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="ID",
            field=models.BigIntegerField(max_length=11),
        ),
    ]