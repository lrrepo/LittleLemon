# Generated by Django 4.2.9 on 2024-01-23 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ID", models.IntegerField(max_length=11)),
                ("Name", models.CharField(max_length=255)),
                ("No_of_guests", models.IntegerField(max_length=6)),
                ("BookingDate", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Menu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ID", models.IntegerField(max_length=5)),
                ("Title", models.CharField(max_length=255)),
                ("Price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("Inventory", models.IntegerField(max_length=5)),
            ],
        ),
    ]