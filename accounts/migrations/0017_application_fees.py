# Generated by Django 4.1.2 on 2023-06-17 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0016_delete_application_fees"),
    ]

    operations = [
        migrations.CreateModel(
            name="Application_Fees",
            fields=[
                ("name", models.CharField(max_length=50)),
                ("amount", models.IntegerField(default=0)),
                (
                    "fees_receipt_no",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                (
                    "academic_year",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.academic_year",
                    ),
                ),
            ],
        ),
    ]