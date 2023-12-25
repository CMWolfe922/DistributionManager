# Generated by Django 4.2.8 on 2023-12-17 10:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("api_manager", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("contact_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("work_number", models.BigIntegerField(null=True)),
                ("mobile_number", models.BigIntegerField(null=True)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="Driver",
            fields=[
                ("driver_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("driver_name", models.CharField(max_length=100)),
                ("driver_email", models.EmailField(max_length=254)),
                (
                    "driver_paperwork",
                    models.FileField(
                        null=True, upload_to="uploads/<driver_name>/<driver_id>/files/"
                    ),
                ),
                ("driver_created", models.DateTimeField(auto_now_add=True)),
                ("dba", models.CharField(max_length=100, null=True)),
                ("driver_start_date", models.DateField(null=True)),
                ("driver_inactive", models.BooleanField(null=True)),
                ("driver_inactive_date", models.DateField(null=True)),
                ("vehicle_type", models.CharField(max_length=25)),
                ("vehicle_make", models.CharField(max_length=25)),
                ("vehicle_model", models.CharField(max_length=25)),
                ("vehicle_year", models.DateField()),
                ("vehicle_color", models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                ("location_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("location_name", models.CharField(max_length=100)),
                ("street_address", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=50)),
                ("zip_code", models.CharField(max_length=20)),
                ("country_code", models.CharField(max_length=50)),
                ("onsite_instructions", models.CharField(max_length=255)),
                ("location_details", models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name="order",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="order",
            name="last_name",
        ),
        migrations.AddField(
            model_name="order",
            name="order_complete",
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="rate",
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="time_open",
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="time_placed",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="time_to_complete",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_id",
            field=models.BigAutoField(
                primary_key=True, serialize=False, unique_for_date="order_placed"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_type",
            field=models.CharField(
                choices=[
                    ("SCHD", "Scheduled"),
                    ("CASH", "Cash Customer"),
                    ("DIST", "Distribution"),
                    ("HTSHOT", "Hot Shot"),
                    ("STAT", "Rush Stat"),
                    ("ONEHR", "One Hour"),
                    ("THRHR", "Three Hour"),
                    ("SAMDAY", "Same Day"),
                ],
                max_length=10,
            ),
        ),
        migrations.CreateModel(
            name="Pickup",
            fields=[
                ("pickup_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("pu_arrival_time", models.DateTimeField()),
                ("pu_depart_time", models.DateTimeField()),
                (
                    "pu_contact",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api_manager.contact",
                    ),
                ),
                (
                    "pu_location",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api_manager.location",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Delivery",
            fields=[
                ("delivery_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("del_arrival_time", models.DateTimeField()),
                ("del_depart_time", models.DateTimeField()),
                (
                    "del_contact",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api_manager.contact",
                    ),
                ),
                (
                    "del_location",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api_manager.location",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("created", models.DateTimeField(auto_now_add=True)),
                ("customer_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("customer_name", models.CharField(max_length=100, unique=True)),
                (
                    "customer_location",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api_manager.location",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="contact",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contacts",
                to="api_manager.customer",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="customer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="api_manager.customer",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="order_del",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="api_manager.delivery",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="order_pu",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="api_manager.pickup",
            ),
        ),
    ]